# -*- coding: utf-8 -*-
"""
# @Time    :  2022/11/10 15:34
# @Author  : linxiaoyi
# @FileName: operationCase.py
#@IDE ：PyCharm
"""
from collections import defaultdict

from utils.excelVarles import excelVarles
from utils.processingRelevant import Relevant
from common.toFunction import Func
import allure
from functools import wraps

def inDict(key, dict):
    if key in dict:
        return str(dict[key])
    else:
        return
def inDict2(key,dict):
    dict_n = defaultdict(str)
    dict_n.update(dict)

def preHeader(headers,relevant_dict_global):
    # headers = data[excelVarles.case_headers]
    if len(str(headers).split()) == 0:
        pass
    elif len(str(headers)) >= 0:
        # headers['Authorization']=login_token
        # headers=headers
        # headers=Relevant.write_case_relevant(headers, relevant_lists)  # 是否需参数化
        headers = Relevant().write_case_relevant2(headers, relevant_dict_global)  # 是否需参数化
        # headers = json.loads(headers)  # 转换为字典
        headers = eval(headers)
    return headers

def preData(params,relevant_dict_global):
    if len(str(params).split()) == 0 or params is None:
        # print("请求参数", params)
        allure.attach('None', "请求参数", attachment_type=allure.attachment_type.TEXT)
        pass
    elif len(str(params)) >= 0:
        # print("请求参数",params)
        allure.attach(params, "请求参数", attachment_type=allure.attachment_type.TEXT)
        # params= Relevant.write_case_relevant(params, relevant_lists) #是否需参数化
        params = Relevant().write_case_relevant2(params, relevant_dict_global)  # 是否需参数化
        # params = func.replacement(params)  # 是否需要执行函数
        params = Func().ExcuteFunction2(params)
        params = params.replace("'", "\"")
    return params
def default_Data(filekey, data):
    def default_preData(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            param=inDict(filekey, data)
            f=func(param,*args,**kwargs)
            return f
        return wrapper

# @default_Data(excelVarles.case_file, 1)
# def fileData():
#     pass

def preParam(params,relevant_dict_global):
    # params = data[excelVarles.case_data]
    if len(str(params).split()) == 0 or params is None:
        # print("请求参数", params)
        allure.attach('None', "请求参数", attachment_type=allure.attachment_type.TEXT)
        pass
    elif len(str(params)) >= 0:
        # print("请求参数",params)
        allure.attach(params, "请求参数", attachment_type=allure.attachment_type.TEXT)
        # params= Relevant.write_case_relevant(params, relevant_lists) #是否需参数化
        params = Relevant().write_case_relevant2(params, relevant_dict_global)  # 是否需参数化
        # params = func.replacement(params)  # 是否需要执行函数
        params = Func().ExcuteFunction2(params)
        params = params.replace("'", "\"")
    return params

def preFile(filekey, data):
    # 对文件上传路径是否为空进行处理
    # files=inDict(filekey, data)
    if filekey in data:
        files = data[filekey]
        print("files:", files)
        if len(str(files).split()) == 0:
            allure.attach('None', "上传文件", attachment_type=allure.attachment_type.TEXT)
            pass
        elif files is None:
            allure.attach('None', "上传文件", attachment_type=allure.attachment_type.TEXT)
            file = files
            return file
        elif len(str(files)) >= 0:
            allure.attach(str(files), "上传文件", attachment_type=allure.attachment_type.TEXT)
            # file = Relevant.write_case_relevant(files, relevant_lists)  # 是否需参数化
            # file = Relevant().write_case_relevant2(str(files), relevant_dict_global)  # 是否需参数化
            # file=files   20221108路径优化
            file = Func().ExcuteFunction2(files)
            file = file.replace("'", "\"")
            return file
    else:
        file = None

def iceParam(data):
    case_ip = inDict(excelVarles.case_ip, data)
    case_port = inDict(excelVarles.case_port, data)
    case_isMocl = inDict(excelVarles.case_isMocl, data)
    case_rootservice = inDict(excelVarles.case_rootservice, data)
    case_model = inDict(excelVarles.case_model, data)
    case_proxyname = inDict(excelVarles.case_proxyname, data)
    case_othmodel = inDict(excelVarles.case_othmodel, data)
    case_modelclass = inDict(excelVarles.case_modelclass, data)
    case_service = inDict(excelVarles.case_service, data)

def sshParam(data):
    ssh_address = inDict2(excelVarles.ssh_address, data)
    # if ssh_address:
    ssh_port = inDict2(excelVarles.ssh_port, data)
    ssh_username = inDict2(excelVarles.ssh_username, data)
    sshpassword = inDict2(excelVarles.sshpassword, data)
    bindport = inDict2(excelVarles.bindport, data)
    host = inDict2(excelVarles.host, data)
    username = inDict2(excelVarles.username, data)
    password = inDict2(excelVarles.password, data)
    dbname = inDict2(excelVarles.dbname, data)
    charset = inDict2(excelVarles.charset, data)
    sql = inDict2(excelVarles.sql, data)
    sql_name = inDict2(excelVarles.sql_name, data)
    auto = inDict2(excelVarles.case_isRun, data)
    # 动态添加模块和标题
    allure.dynamic.feature(data[excelVarles.fileName])  # feature>story>title
    allure.dynamic.story(data[excelVarles.sheetName])
    allure.dynamic.title(sql_name)  # 报告用例名称
    allure.title(sql_name)