# -*- coding: utf-8 -*-
"""
# @Time    :  2022/10/31 17:14
# @Author  : linxiaoyi
# @FileName: operationSql.py
#@IDE ：PyCharm
"""
from robotide.lib.robot.api import logger
from pymysql import cursors, connect
from sshtunnel import SSHTunnelForwarder
from robot.api import logger
import logging
import importlib

class FMSQL(object):
    def __init__(self,ssh_address=None,ssh_port=None,ssh_username=None,ssh_password=None,bindport=None, host=None, username=None, password=None, dbname=None,charset=None):
        if ssh_address is None and ssh_port is None and ssh_username is None and ssh_password is None and bindport is None and username is None and password is None and dbname is None and charset is None:
            self.ssh_address ="120.24.43.28"
            self.ssh_port = 2201
            self.ssh_username = "fsmeeting"
            self.ssh_password = "fsmeeting123"
            self.bindport = 3306
            self.host='127.0.0.1'
            self.username = "fsboss"
            self.password = "fsboss"
            self.dbname = "fsboss"
            self.charset ="utf8"
        else:
            self.ssh_address = ssh_address
            self.ssh_port = ssh_port
            self.ssh_username = ssh_username
            self.ssh_password = ssh_password
            self.bindport = bindport
            self.host = host
            self.username = username
            self.password = password
            self.dbname = dbname
            self.charset=charset
        self.max_connect_cnt = 20
        # self.mysqltest(ssh_address, ssh_port, ssh_username, ssh_password, bindport, username, password, dbname,charset)
        self.Error = False

    def mysqltest(self):
        # 设置ssh的跳板机的连接信息
        # 设置通过跳板机所要连接的MySQL服务器地址和端口（如果跳板机本身就是MySQL服务器，则直接填写'127.0.0.1'）
        # 一定注意开启后，要关闭服务，某些情况下，忘关闭服务会带来异常
        try:
            # if self.ssh_address is None and self.ssh_port is None and self.ssh_username is None and self.ssh_password is None :
            if not self.ssh_address and not self.ssh_port and not self.ssh_username  and not self.ssh_password :
                db_connect=self.straight_db_connect()
            else:
                self.server = SSHTunnelForwarder(ssh_address_or_host=self.ssh_address, ssh_port=self.ssh_port,
                                                 ssh_username=self.ssh_username, ssh_password=self.ssh_password,
                                                 remote_bind_address=('127.0.0.1',self.bindport))
                try:
                    self.server.start()
                    db_connect=self.db_connect(self.server)
                except Exception as e:
                     print(e)
        except Exception as e:
            print(e)

    def db_connect(self,server):
        connect_cnt = 0
        while True:
            try:
                self.db = connect(self.host,self.username,self.password,self.dbname,port=server.local_bind_port,charset='utf8')
            except Exception as e:
                # 当连接过多的时候或者其他异常的时候则sleep 1秒则重新连接
                # time.sleep(1) #这个可以注释掉
                connect_cnt += 1
                if connect_cnt < self.max_connect_cnt:
                    pass
                else:
                    raise e
            else:
                break
        self.cursor = self.db.cursor()

        # db = connect(
        #     host='127.0.0.1', user=username, password=password, db=dbname, port=server.local_bind_port, charset=charset)
        # return db
    def straight_db_connect(self): #直连
        connect_cnt = 0
        while True:
            try:
                self.db = connect(host=self.host,port=self.bindport,user=self.username,passwd=self.password,db=self.dbname,charset='utf8')
            except Exception as e:
                connect_cnt += 1
                if connect_cnt < self.max_connect_cnt:
                    pass
                else:
                    raise e
            else:
                break
        self.cursor = self.db.cursor()

    # 装饰器函数保证更新数据的时候，连接OK，如果连接不正确重新连接
    def reconnectdb(func):
        def wrapfunc(self, sql=''):
            try:
                self.db.ping()
            except:
                self.db_connect()
            self.Error = False
            return  func(self, sql)
        return wrapfunc
        # 插入数据

    @reconnectdb
    def insertdb(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            # Rollback in case there is any error
            print("Error: unable to insertdb!")
            self.db.rollback()
            self.Error = True

    # 更新数据
    @reconnectdb
    def updatedb(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            # Rollback in case there is any error
            print("Error: unable to updatedb!")
            self.db.rollback()
            self.Error = True

    # 删除数据
    @reconnectdb
    def deldb(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # Rollback in case there is any error
            print("Error: unable to deldb!")
            self.db.rollback()
            self.Error = True
    # 获取数据
    @reconnectdb
    def selectdb(self, sql,sansTran=False,returnAsDict=False):
        cur = None
        try:
            cur = self.cursor
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            if returnAsDict:
                mappedRows = []
                col_names = [c[0] for c in cur.description]

                for rowIdx in range(len(results)):
                    d = {}
                    for colIdx in range(len(results[rowIdx])):
                        d[col_names[colIdx]] = results[rowIdx][colIdx]
                    mappedRows.append(d)
                return mappedRows

            return results
        except Exception as e:
            print("Error: unable to fecth data")
            self.Error = True
        finally:
            if cur:
                if not sansTran:
                    self.db.rollback()

    @reconnectdb
    def row_count(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            rowc=self.cursor.rowcount
            return rowc
        except Exception as e:
            print("Error: unable to fecth data")
            self.Error = True
    # 关闭数据
    def closedb(self):
        try:
            self.db.close()
            self.server.close()
        except:
            print ("数据库已关闭，无需关闭")

    def check_if_exists_in_database(self, sql,sansTran=False):
        logger.info ('Executing : Check If Exists In Database  |  %s ' % sql)
        if not self.selectdb(sql, sansTran):
            raise AssertionError("Expected to have have at least one row from '%s' "
                                 "but got 0 rows." % sql)

    def check_if_not_exists_in_database(self, sql, sansTran=False):
        logger.info('Executing : Check If Not Exists In Database  |  %s ' % sql)
        queryResults = self.selectdb(sql)
        if queryResults:
            raise AssertionError("Expected to have have no rows from '%s' "
                                 "but got some rows : %s." % (sql, queryResults))
if __name__ == '__main__':
    a = FMSQL(ssh_address='120.24.43.28', ssh_port=2201, ssh_username='fsmeeting', ssh_password='fsmeeting123',
              bindport=3306, username='fsboss', password='fsboss', dbname='fsboss', charset='utf8')
    db = a.mysqltest()
    sql0 = 'SELECT userid FROM t_userinfo where companyid="55095";'
    test = a.selectdb(sql0)
    d = a.closedb()
    print(test)