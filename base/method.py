# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/12 15:41
@Auth ： linxiaoyi
@File ：method.py
@IDE ：PyCharm

"""

import requests
import json
import Ice
from pathlib import Path
import traceback,sys,importlib,os
import inspect
import logging
import slicepy2

class ApiRequest(object):
    def __init__(self):
        pass
    def send_request(self,method,url,data=None,params=None,headers=None,cookies=None,json=None,files=None,auth=None,timeout=None,proxies=None,verify=None,cert=None,
                     PaIsMoCl=0, rootService=None, ip=None, port=0, model=None, othermodel=None, ModelClass_name=None,proxy_name=None, iceservice=None):
        if method.upper() == 'ICE':
            self.res=self.request_ice(PaIsMoCl=PaIsMoCl,rootService=rootService,ip=ip,port=port,model=model,othermodel=othermodel,ModelClass_name=ModelClass_name,proxy_name=proxy_name,iceservice=iceservice,params=params)
        else:
            if files:
                self.res= self.upload(method, url, files, data=data, params=params, headers=headers, cookies=cookies, json=json, auth=auth,timeout=timeout, proxies=proxies, verify=verify, cert=cert)
            else:
                self.res=requests.request(method=method,url=url,data=data,params=params,headers=headers,cookies=cookies,json=json,files=files,auth=auth,timeout=timeout,proxies=proxies,verify=verify,cert=cert)

        return self.res


    def upload(self,method,url,files,data=None,params=None,headers=None,cookies=None,json=None,auth=None,timeout=None,proxies=None,verify=None,cert=None):
        # print("upload.files:", type(files))
        # print("method:{}.url:{},files:{}".format(method,url,files))
        # print("headers:{}".format(headers))
        # fileparam = eval(repr(files))
        fileparam = eval(files)
        print("fileparam:",fileparam)
        for key in fileparam:
            # fileparam[key]=os.path.abspath(fileparam[key]) #20221108优化路径转义字符
            openfile = open(fileparam[key], 'rb')
            importfile = {key: openfile}
        res=requests.request(method=method,url=url,data=data,params=params,headers=headers,cookies=cookies,json=json,files=importfile,auth=auth,timeout=timeout,proxies=proxies,verify=verify,cert=cert)
        openfile.close()
        return res

    def request_ice(self,PaIsMoCl=0,rootService=None,ip=None,port=0,model=None,othermodel=None,ModelClass_name=None,proxy_name=None,iceservice=None,params=None):
        '''
        :param :PaIsMoCl:请求接口时，参数需要调用另一个模块的类的返回值作为入参则为1；直接用*args入参，则为0
        :param :rootService:接口模块的根文件名
        :param :ip:服务器地址
        :param port: 服务器端口
        :param model: 被测服务根模块名
        :param proxy_name: 代理的方法名
        :param othermodel: 参数需要调用另一个模块时，另一个模块名
        :param ModelClass_name: 参数需要调用另一个模块的类，该类名
        :param iceservice: 被测服务名（具体）
        :param params:被测服务参数
        :param varname:被测服务参数名
        :return: 打印接口返回值
        '''
        # path=Path('./').cwd().parent.joinpath('slicepy2')
        path = Path('./').cwd().joinpath('slicepy2')
        path_new=str(path).replace('\\', '\\\\')
        sys.path.insert(0, path_new)
        self.status=0
        ic=None
        try:
            ic=Ice.initialize(sys.argv) # 初始化运行环境
            Ip="%s:default -h %s -p %s"%(str(rootService),str(ip),str(port))
            base=ic.stringToProxy(Ip)
            import_model=importlib.import_module(model)
            cls=inspect.getmembers(import_model,inspect.isclass)
            proxy=getattr(import_model,proxy_name)
            Service=proxy.checkedCast(base)

            if not Service:
                raise RuntimeError("Invalid Proxy")
            else:
                if PaIsMoCl == 1:  # 请求接口时，参数需要调用另一个模块的类
                    import_othermodel=importlib.import_module(othermodel)
                    if isinstance(params, dict):
                        ModelClass_params = getattr(import_othermodel, ModelClass_name)(**params)
                    else:
                        ModelClass_params=getattr(import_othermodel,ModelClass_name)(*params)
                    print("ModelClass_params:",ModelClass_params)
                    res = getattr(Service, iceservice)(ModelClass_params)
                    print("=================================================")
                elif PaIsMoCl == 0: # 请求接口时，参数不需要调用另一个模块的类，直接使用输入的参数
                    if isinstance(params, dict):
                        res=getattr(Service,iceservice)(**params)
                    else:
                        res = getattr(Service, iceservice)(*params)

                elif PaIsMoCl == 2:#请求commonService调用接口
                    params = list(params)
                    if len(params) == 3:
                        byarray = bytearray(params[2], encoding='utf-8')
                        import_othermodel = importlib.import_module(othermodel)
                        ModelClass_params = getattr(import_othermodel, ModelClass_name)(params[0], params[1], byarray)  # 调用的类
                        tresutlt = Service.invoke(ModelClass_params)
                        res = tresutlt[1].result.decode('utf-8')
                    else:
                        res=None
                        res = "params is invalid"
                else:
                    res=None
                    res = "PaIsMoCl is invalid value"
                return res

        except:
            e=traceback.print_exc()
            self.status = 1
            logging.info("出现异常，异常消息：" + str(e))
            # return 'Fail'
        finally:
            if ic:
                # Clean up
                try:
                    ic.destroy()
                    print("--------------------------------------------------------------------------------")
                except:
                    traceback.print_exc()
                    self.status = 1

        sys.exit(self.status)

 # def request_Ice(self,PaIsMoCl=0,rootService='',ip='', port=0, model='', proxy_name='', othermodel='', ModelClass_name='', iceservice='',param={},varname=()):
 #        '''
 #        :param :PaIsMoCl:请求接口时，参数需要调用另一个模块的类的返回值作为入参则为1；直接用*args入参，则为0
 #        :param :rootService:接口模块的根文件名
 #        :param :ip:服务器地址
 #        :param port: 服务器端口
 #        :param model: 被测服务根模块名
 #        :param proxy_name: 代理的方法名
 #        :param othermodel: 参数需要调用另一个模块时，另一个模块名
 #        :param ModelClass_name: 参数需要调用另一个模块的类，该类名
 #        :param iceservice: 被测服务名（具体）
 #        :param params:被测服务参数
 #        :param varname:被测服务参数名
 #        :return: 打印接口返回值
 #        '''
 #        new_path=os.path.join(os.getcwd(), 'slicepy2')
 #        #sys.path.append(os.path.join(os.getcwd(), rootService))
 #        sys.path.insert(0, new_path)
 #        # print("sys.path:", sys.path)
 #        icecall=ICE_call.ICECall() #
 #        self.status = 0
 #        ic = None
 #        try:
 #            # 初始化运行环境
 #            ic = Ice.initialize(sys.argv)
 #
 #            # 获取远程companyService服务的代理
 #            Ip = str(rootService) + ":default -h " + str(ip) + " -p " + str(port)
 #            base = ic.stringToProxy(Ip)
 #            import_model = importlib.import_module(model)  # 动态导入com.fastonz.fmserver.companyMgr
 #            cls = inspect.getmembers(import_model, inspect.isclass)
 #            # print("类：",cls)
 #            proxy = getattr(import_model, proxy_name)  # CompanyServicePrx类
 #            # print(proxy)
 #            Service = proxy.checkedCast(base)
 #
 #            if not Service:
 #                raise RuntimeError("Invalid Proxy")
 #
 #            # 远程调用，看起来像本地的服务一样
 #            if PaIsMoCl == 1:  # 请求接口时，参数需要调用另一个模块的类
 #                import_othermodel = importlib.import_module(othermodel)
 #                ModelCl = getattr(import_othermodel, ModelClass_name)  # 调用的类
 #                t = icecall.GetinitVarNotSelf(ModelCl)  # 提取调用类所需的参数对应的参数名
 #                a = icecall.DictToArgs(param, t)  # 入参（字典）按照提取的参数名的顺序排序
 #                params = ModelCl(*a)  # *a 一个列表里的各个值作为单独的参数传递
 #                print("ssssssparams：",params)
 #                res = eval('Service.%s' % iceservice)(params)  # 把string变量转换成相应函数
 #                print("=================================================")
 #            elif PaIsMoCl == 0:  # 请求接口时，参数不需要调用另一个模块的类，直接使用输入的参数
 #                varlist = list(varname)
 #                a = icecall.DictToArgs(param, varname)  # 入参（字典）按照提取的参数名的顺序排序
 #                # print(type(a))
 #                try:
 #                    if isinstance(a, dict):
 #                        res = eval('Service.%s' % iceservice)(**a)  # 把string变量转换成相应函数
 #                    else:
 #                        res = eval('Service.%s' % iceservice)(*a)  # 把string变量转换成相应函数
 #                except Exception as e:
 #                    res=str(e)
 #            elif PaIsMoCl==2:  #请求commonService调用接口
 #                params=list(param)
 #                if len(params)==3:
 #                    byarray=bytearray(params[2],encoding='utf-8')
 #                    import_othermodel = importlib.import_module(othermodel)
 #                    ModelCl = getattr(import_othermodel, ModelClass_name)  # 调用的类
 #                    # model=com.hst.boss.model.Request(params[0],params[1],byarray)
 #                    model= ModelCl(params[0],params[1],byarray)
 #                    tresutlt=Service.invoke(model)
 #                    res = tresutlt[1].result.decode('utf-8')
 #                else:
 #                    res="params is invalid"
 #            else:
 #                res="PaIsMoCl is invalid value"
 #            return res
 #
 #        except:
 #            e=traceback.print_exc()
 #            self.status = 1
 #            logging.info("出现异常，异常消息：" + str(e))
 #            # return 'Fail'
 #        finally:
 #            if ic:
 #                # Clean up
 #                try:
 #                    ic.destroy()
 #                    print("--------------------------------------------------------------------------------")
 #                except:
 #                    traceback.print_exc()
 #                    self.status = 1
 #
 #        sys.exit(self.status)






if __name__ == '__main__':
    from urllib.parse import urlencode
    import json
    from pathlib import Path
    # url = 'https://oauth.haoshitong.com/oauth2/token'
    # headers = {"content-type": "application/x-www-form-urlencoded",
    #            "Authorization": "Basic aDUtY2xpZW50OjczNzlkYjFhLWUxNzMtNGM4ZS04OTVkLTNiNGMzOTMzOWU1OA=="}
    # data = {"grant_type": "password", "username": "testpy@hst.com", "password": "123456"}
    # to_data=eval(str(data))
    ApiRequest=ApiRequest()
    # res=ApiRequest.send_request(method='post',url=url,headers=headers,data=to_data)
    # access_token=res.json()['access_token']
    # # print("res：",res)
    # # print("text：",res.text)
    # # print("json：",res.json)
    # upload_url="https://bss-api.haoshitong.com/api/meetings/948947/authorizations/excel"
    # upload_header={"Authorization":"bearer "+access_token}
    # file=json.dumps({"file":"F:\\Test\\Interface\\Python自动化\\project_new\\data\\会议授权模板管理员.xlsx"})
    # uplod_res = ApiRequest.upload(method='post', url=upload_url, headers=upload_header, files=file)
    # uplod_res2=ApiRequest.send_request(method='post',url=upload_url,files=file,headers=upload_header)
    #
    # print("res：",uplod_res)
    # print("text：",uplod_res.text)
    # print("json：",uplod_res.json)

    # sys.path.append("F:\\Test\\Interface\\Python自动化\\git_api\\test\\slicepy2")
    # rootService = 'companyService'
    # ip = '47.113.118.87'
    # port = 33001
    # model = 'com.fastonz.fmserver.companyMgr'
    # proxy_name = 'CompanyServicePrx'
    # iceservice = 'GetCompanyLicenseCount'
    # params = {'companyID':46425, 'servicesID':1}
    # ApiRequest.request_ice(rootService,ip,port,model,proxy_name,iceservice,params)
    PaIsMoCl = 1,
    rootService = 'roomService'
    ip = '47.113.118.87'
    port = 33001
    model = 'com.fastonz.fmserver.roomMgr'
    othermodel = 'com.fastonz.fmserver.model'
    ModelClass_name = 'RoomRouteModel'
    proxy_name = 'RoomServicePrx'
    iceservice = 'UpdateRoomRouteInfo'
    params = ("aaaa", 111, "bbbb", "cccc", "ddddfff", 222, "ffff", "gggg", "hhhh", 333)
    # params={'roomID': 33164, 'serviceID': 1075, 'userName': 'scott', 'userIP': '192.168.1.23', 'isLogin': 1, 'eventCode': 1,
    #  'eventDesc': 'fdsfsa', 'companyID': 595}
    ApiRequest.send_request(method='ice',url='',PaIsMoCl=1,rootService=rootService,ip=ip,port=port,model=model,othermodel=othermodel,ModelClass_name=ModelClass_name,proxy_name=proxy_name,iceservice=iceservice,params=params)


