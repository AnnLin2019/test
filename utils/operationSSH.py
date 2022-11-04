# -*- coding: utf-8 -*-
"""
# @Time    :  2022/10/26 16:03
# @Author  : linxiaoyi
# @FileName: operationSSH.py
#@IDE ：PyCharm
"""
import re

import paramiko


class Ssh2():
    # def __init__(self,path,sheetname):
    #     self.operate_excel = operate_excel.excel(path, sheetname)

    def ssh2(self,ip,port,username,password,cmd):
        try:
            ssh=paramiko.SSHClient() #创建一个客户端
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #创建一个白名单
            ssh.connect(ip,port,username=username,password=password,timeout=10)
            list=[]
            for m in cmd:
                stdin,stdout,stderr=ssh.exec_command(m)
                stdin.write("Y")
                out=stdout.readlines()
                # for o in out:
                #     print("o:",o)
                # print(out[0])
                list.append(out[0])
            # print(list)
            print("%s\tOK\n"%ip)
            ssh.close()
            return list

        except Exception as e:
            print("%s\tError\t%s\n"%(ip,e))


    def Strmatch(self,patternstr,string):
        if patternstr=='':
            s=string
        elif patternstr==None:
            s = string
        else:
            pattern = re.compile(patternstr,re.I)
            m = pattern.search(string)
            s=m.group(1)
        return s

    def Isssh(self, string, keyword):
        if string.find(keyword) >= 0:
            return True
        else:
            return False

    def Isssh2(self,dict,keyword):
         if keyword in dict.keys():
             return True
         else:
             return False

    def Ispattern(self,ip, port, username, password, cmd,pattern=None):
        result=[]
        key=[]
        out = self.ssh2(ip, port, username, password, cmd) #找单元格是否有值，找内容是否有pattern字段
        print(out)
        try:

            if len(out) > 0:
                if pattern:
                    diff = len(out) - len(pattern)
                    for i in range(len(pattern)):
                        keyname = 'out' + str(i)
                        key.append(keyname)
                        if pattern[i]:
                            data = self.Strmatch(pattern[i], out[i]) #按正则获取返回值
                            result.append(data)
                        else:
                            result.append(out[i])
                    if diff!=0:
                        for i in range(diff):
                            j = i + len(pattern)
                            keyname = 'out' + str(j)
                            key.append(keyname)
                            result.append(out[j])
                            print(out[j])
                else:
                    for i in range(len(out)):
                        keyname = 'out' + str(i)
                        key.append(keyname)
                        result.append(out[i])
            Ldata=dict(zip(key,result))
        except Exception as e:
            Ldata=str(e)
            # print(e)
        # self.operate_excel.WriteResult(2,3,Ldata)                   #写入提取的值，以dict格式写入：关联值的形式
        return Ldata
    def SshResult(self,ssh):
        # Isssh = self.Isssh2(testcase_dict, keyword)
        # if Isssh:
        #     ssh = testcase_dict["ssh"]
            param = eval(ssh)
            print("param==",param)
            print(type(param))
            ip = param['ip']
            port = param['port']
            username = param['username']
            password = param['password']
            cmd = param['cmd']
            if ssh.find('pattern') >= 0:  # 返回结合是否需要正则处理
                pattern = param['pattern']
                result=self.Ispattern(ip, port, username, password, cmd, pattern)
            else:
                result=self.Ispattern(ip, port, username, password, cmd)
            return result

if __name__ == '__main__':
    c=str({'ip':'47.113.118.87','port':2201,'username':'fsmeeting','password':'fsmeeting123','cmd':["tac /fsmeeting/logs/dal.log |grep -E 'id .*? input data should be .*?'"],'pattern':['input data should be (.*)']})
    Operate_ssh = Ssh2()
    res=Operate_ssh.SshResult(c)
    print(res)
    cmd=["tac /fsmeeting/logs/dal.log |grep -E 'id .*? input data should be .*?'"]
    pattern= ['input data should be (.*)']
    Operate_ssh.ssh2('47.113.118.87','2201','fsmeeting','fsmeeting123',cmd)
