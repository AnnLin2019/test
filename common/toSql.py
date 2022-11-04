# -*- coding: utf-8 -*-
"""
# @Time    :  2022/10/31 17:50
# @Author  : linxiaoyi
# @FileName: toSql.py
#@IDE ：PyCharm
"""
from utils import operationSql


class Exesql:
    def execute_sql(self,sql,ssh_address=None,ssh_port=None,ssh_username=None,ssh_password=None,bindport=None, host=None, username=None, password=None, dbname=None,charset=None):
        try:
            if sql:
                FMSQL = operationSql.FMSQL(ssh_address=ssh_address,ssh_port=ssh_port,ssh_username=ssh_username,ssh_password=ssh_password,bindport=bindport,host=host,username=username,password=password,dbname=dbname,charset=charset)
                db = FMSQL.mysqltest()
                sqllist=sql.split(" ")
                sql_lower=sqllist[0].lower()
                # print(sql_lower)
                List=["select","update","insert","delete"] #判断输入的语句 是查询、更新、插入还是删除
                if sql_lower.find(List[0])!=-1:
                    result = FMSQL.selectdb(sql)
                elif sql_lower.find(List[1])!=-1:
                    result = FMSQL.updatedb(sql)
                elif sql_lower.find(List[2])!=-1:
                    result = FMSQL.insertdb(sql)
                elif sql_lower.find(List[3])!=-1:
                    result = FMSQL.deldb(sql)
                else:
                    result=""
                    pass
                FMSQL.closedb()
                return result
        except Exception as e:
            result="Error"
            print(e)
            return result


if __name__ == '__main__':
    Exesql=Exesql()
    sql0 = 'SELECT userid FROM t_userinfo where companyid="55095";'
    # res=Exesql.execute_sql(sql0,ssh_address='120.24.43.28', ssh_port=2201, ssh_username='fsmeeting', ssh_password='fsmeeting123',
    #           bindport=3306, username='fsboss', password='fsboss', dbname='fsboss', charset='utf8')
    # print(res)
    sql1='SELECT * FROM t_userinfo where UserID=1460586;'
    res2 = Exesql.execute_sql(sql1, ssh_address='', ssh_port='', ssh_username='',
                             ssh_password='',
                             bindport='', host='192.168.5.69',username='fsboss', password='fsboss', dbname='fsboss', charset='utf8')
    print(res2)