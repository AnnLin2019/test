# -*- coding: utf-8 -*-
"""
# @Time    :  2022/10/20 14:49
# @Author  : linxiaoyi
# @FileName: toFunction.py
#@IDE ：PyCharm
"""
import importlib,re
from functools import wraps

class Func:
    def param_type(self,func,param):
        if isinstance(param,tuple):
            return func(*param)
        elif isinstance(param,dict):
            return func(**param)
        else:
            return func(param)

    def DoFun(self,funcs):
        Isfunction = funcs.find('.')
        if Isfunction > 0:
            funcstr1 = funcs.split('.', 1)
            # print("funcstr1:", funcstr1)
            justfun = funcstr1[0].split("'")
            if justfun:
                fungroup = justfun[-1]

            else:
                fungroup = funcstr1[0]
            module = importlib.import_module(str(fungroup))
            funlist = funcstr1[1].split('.')
            # print("funlist***:", funlist)
            for i in range(len(funlist)):
                pat = re.compile(r"(.+?)\((.*?)\)")
                # print("funlist[i]:", funlist[i])
                search_param = re.search(pat, funlist[i])
                # print("search_param:", search_param)
                if search_param:
                    if search_param.group(2):
                        params = (search_param.group(2))
                        try:
                            function = getattr(funlist[i - 1], search_param.group(1))  # 函数
                            Excfun = function(*eval(params))
                        except Exception:
                            function = getattr(module, search_param.group(1))  # 函数
                            # Excfun = function(*eval(params)) 20221108y优化函数执行
                            Excfun=self.param_type(function,eval(params))
                            print(Exception)

                    else:
                        try:
                            Excfun = getattr(funlist[i - 1], search_param.group(1))()
                        except:
                            Excfun = getattr(module, search_param.group(1))()
                else:
                    try:
                        Excfun = getattr(Excfun, funlist[i])
                    except:
                        # Excfun = getattr(module, funlist[i])
                        module = importlib.import_module(str(fungroup)+'.'+funlist[i])
        return Excfun

    def multi_sub(self,s,old,new):
        pass

    def ExcuteFunction(self, funcstr):
        funcstr = str(funcstr)
        Isfunction = funcstr.find('.')  # 找不到返回-1，找到了都返回下标
        if Isfunction > 0:
            funcstr1 = funcstr.rsplit('.', 1)  # 只分割最后一个（rsplit的使用）
            len(funcstr)
            module = funcstr1[0]
            import_model = importlib.import_module(module)
            # print(import_model)
            # Excfun=eval(funcstr)
            m = funcstr1[-1].split('(')  # 分割函数和入参
            F = m[0]  # 提取函数
            function = getattr(import_model, F)
            paramstr = "(" + m[-1]  # 提取入参，()格式的字符串
            params = eval(paramstr)  # ()格式的字符串转换为数组
            Excfun = function(*params)
            return Excfun
        else:
            Excfun = ""
            return Excfun

    def ExcuteFunction2(self, funcstr):
        self.funcstr = str(funcstr)
        # try:
        #     Excfun=eval(funcstr)
        #     print('111')
        # except NameError:

        findcode = re.compile("\$<(.+?)>")
        # funcs=findcode.search(funcstr)
        funcs=findcode.findall(self.funcstr)
        # print("findall:",findcode.findall(self.funcstr))
        fundict={}
        fuclist=[]
        if funcs:
           for i in range(len(funcs)):
                funcname = funcs[i].strip("'}").strip("'").strip("}")
                # print("函数{}".format(funcname))
                Excfun=self.DoFun(funcs[i])
                fundict={}
                fundict[funcname]=str(Excfun)
                fuclist.append(fundict)
                self.funcstr=self.funcstr.replace('$<' + funcname + '>', str(Excfun),1)
           #      print("funcstr",self.funcstr)
           # print("fundict：",fundict)
           # print("fuclist:",fuclist)
           # print("self.funcstr",self.funcstr)
        else:
            Excfun = ""
            funcname=""
            fundict[funcname] = str(Excfun)
            fuclist.append(fundict)
            self.funcstr = self.funcstr
        # return str(Excfun),funcname
        return self.funcstr



    def replacement(self, s): #支持"random.randint(10,99)\"+\"DD20221010"格式
        code = re.compile(r'(.+?)\"\+\"(.+)')
        # print("s:",type(s))

        # print("match.group(1) {}, match.group(2) {}".format(match.group(1), match.group(2)))
        # for fuc in [match.group(1), match.group(2)]:
        try:
            rstr=[]
            for i in range(1,3):
                value,funcname = self.ExcuteFunction2(code.match(s).group(i))
                # print("value:", value)
                if not value:
                    # print("----------------")
                    value = code.match(s).group(i)
                rstr.append(str(value))
            restr=''.join(rstr)
            # print("restr:",restr)
        except AttributeError:
            value,funcname = self.ExcuteFunction2(s)
            # print("s:", s)
            # print("funcname:",funcname)
            # restr=s.replace(funcname,value)
            restr = s.replace('$<'+funcname+'>', value)
            # exec(match.group(2))
        except:
            restr=s
            # print("value0:",restr)
        # print(code.sub(excel.replacement, funcstr))
        return restr

    def replacement2(self, s):
        try:
            value, funcname = self.ExcuteFunction2(s)
            # print("s:", s)
            # print("funcname:", funcname)
            # print("value:",type(value))
            # restr=s.replace(funcname,value)
            restr = s.replace('$<' + funcname + '>', value)
            # exec(match.group(2))
        except:
            restr = s
        return restr

    def replacement3(self, s):
        fuclist=self.ExcuteFunction2(s)
        pass

    def ExcelToFunc2(self,circle_object,testcase_dict,paramkey):
        data=str(testcase_dict[paramkey])
        if data:     #字典值存在true false null值，dict会转换失败
            if data.find('null') > 0:
                data = re.sub('null', '""', data)
            if data.find('true') > 0:
                data = re.sub('true', 'True', data)
            if data.find('false') > 0:
                data = re.sub('false', 'False', data)

        param=eval(data)
        if self.params_relevant.typeof(param) == 'str':
            chdparam=eval(param)
            if self.params_relevant.typeof(chdparam)=='dict':
                for key in chdparam.keys():
                    if chdparam[key].find('.') + chdparam[key].find('(') > 0:
                        chdparam[key] = self.ExcuteFunction(chdparam[key])
                        # chdparam[key] = self.replacement(chdparam[key])
                        testcase_dict[paramkey]=chdparam
                        circle_object.ParamsWrite(testcase_dict, paramkey)
            return chdparam
        elif self.params_relevant.typeof(param)=='dict':
            chdparam = param
        # values=chdparam.values()
            for key in chdparam.keys():
                if str(chdparam[key]).find('.')>0 and str(chdparam[key]).find('(') >0:
                    chdparam[key]=self.ExcuteFunction(chdparam[key])
                    # chdparam[key] = self.replacement(chdparam[key])
                    testcase_dict[paramkey] = chdparam
                    circle_object.ParamsWrite(testcase_dict, paramkey)
            return chdparam
        elif self.params_relevant.typeof(param) == 'list':
            return param

if __name__ == '__main__':
    func=Func()
    # d=str({"userName": "$<random.randint(13000000000,13999999999)>"})
    d=str({"userName": "$<random.randint(10,99)>DD20221010"})
    c=str({"orderId": "$<uuid.uuid1().hex>","crmOrderNo":"DD20221025$<random.randint(1000,9999)>","orderId2": "$<uuid.uuid1().hex>"})
    # c=str({"orderId": ""})
    # f=func.replacement(d)
    # print("----------f-----------",f)
    f2 = func.ExcuteFunction2(c)
    print("----------f2-----------",f2)
    funcs = "$<common.RSA_encrypt.crack_pwd('123456','MHwwDQYJKoZIhvcNAQEBBQADawAwaAJhAJlF0u37iq0aK1kwF+YO9xYrf2SGL8MDtYARczE8LxFt3aIOL0M1hsaKDSDXrwV5M+4F4tAz4ZVHoNWKjB1IN3Xp3KHHKaVMdqMTYQ/VhBbRkEs3y1n/j1gedeISAiYymwIDAQAB')>"
    f3=func.ExcuteFunction2(funcs)
    print(f3)
    f4='$<config.config.data_path3("data")>'
    f5=func.ExcuteFunction2(f4)
    print('---f5---',f5)
    file='F:\\Test\\Interface\\Python自动化\\git_api\\test\\data\\员工导入2.xlsx'
    dd=repr("{'file':file}")
    p=eval(dd)
    import os

    print("curdir",os.path.abspath(os.path.curdir))
    pp=os.path.abspath('F:\\Test\\Interface\\Python自动化\\git_api\test\\data\\员工导入2.xlsx')
    pat='\\'
    a=r'{}'.format(repr('F:\\Test\\Interface\\Python自动化\\git_api\test\\data\\员工导入2.xlsx'))
    print(p)
    ff=open(p,'rb')
    ff.close()



    # import importlib
    # m=importlib.import_module("common")
    # getattr(m,'RSA_encrypt')
    # print(d.replace('$<' + "random.randint(10,99)" + '>', str(98)))
    # dd = str({"userName": "$<random.randint(13000000000,13999999999)>"})
    # findfunc = re.compile("\$<(.+?)>")
    # print(findfunc.search(dd)[1])



    # code=re.compile(r"\'(.+?\..+?)\'")
    # print(code.search(d)[1])
    # match= re.findall(r"['\"](.*?(\.).*?)['\"]",d)
    # match = re.findall(r"['\"](.+?\..+?)['\"]", d)
    # print(match[-1])
    # list1=d.split("'")
    # l=[]
    # for list in list1:
    #     match = re.search(r"(.+\..+)", list)
    #     if match:
    #         print(match[1])
    #         l.append(match[1])
    # print(l)
    # a=' '.join(match[0].split('\n'))
    # print(a)
