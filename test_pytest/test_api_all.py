# -*- coding: utf-8 -*-
"""
# @Time    :  2022/9/13 18:39
# @Author  : linxiaoyi
# @FileName: test_api_all.py
#@IDE ：PyCharm
"""
import pytest
import json
import subprocess
import allure

#参数化运行所有用例
from base.method import ApiRequest
from common import login
from utils.excelVarles import excelVarles
from utils.operationExcel import operationExcel
import logging
import os
import re
from urllib.parse import urlencode
from utils.processingRelevant import Relevant

path='F:\\Test\\Interface\\Python自动化\\git_api\\test\\data\\boss_ice_1.xlsx'
operationexcel=operationExcel(path)
excel = operationexcel .get_allvalue()
login_token=login.login_token
Relevant=Relevant()
# print(login_token)
global relevant_dict_global,relevant_lists
relevant_dict_global={}
relevant_lists=[]
# print("全局type(relevant_dict_global)",type(relevant_dict_global))
@pytest.fixture()
def get_case_name():
    case_name = str(excel[excelVarles.case_name])
    return case_name

@pytest.mark.parametrize('data',excel) #装饰器进行封装用例
@allure.title(get_case_name)
# @allure.title(excel[excelVarles.case_name])
# @allure.feature('报告出来了吗')
# @pytest.mark.parametrize('relevant_dict_global',relevant_dict_global) #装饰器进行封装用例
def test_api_all(data):
    global relevant_dict_global
    # relevant_dict_global = relevant_dict_global
    # print("开始type(relevant_dict_global)",type(relevant_dict_global))

    #获取是否自动化
    auto=data[excelVarles.case_isRun]
    if str(auto).upper=='NO' or None:
        pytest.skip("this test is skipped")

    # 获取参数关联封装
    relevant = data[excelVarles.case_relevant]

    #对请求头为空处理并添加token
    headers=data[excelVarles.case_headers]

    if len(str(headers).split())==0:
        pass
    elif len(str(headers))>=0:
        # headers['Authorization']=login_token
        # headers=headers
        # headers=Relevant.write_case_relevant(headers, relevant_lists)  # 是否需参数化
        headers = Relevant.write_case_relevant2(headers, relevant_dict_global)  # 是否需参数化
        # headers = json.loads(headers)  # 转换为字典
        headers = eval(headers)

    #对请求参数为空进行处理
    params=data[excelVarles.case_data]
    if len(str(params).split())==0:
        pass
    elif len(str(params))>=0:
        # print("relevant_params_before:", params)
        # params=params
        # print("relevant_list是",relevant_list)
        # params= Relevant.write_case_relevant(params, relevant_lists) #是否需参数化
        params = Relevant.write_case_relevant2(params, relevant_dict_global)  # 是否需参数化
        params=params.replace("'","\"")



    #对文件上传路径是否为空进行处理
    if excelVarles.case_file in data:
        files=data[excelVarles.case_file]
        if len(str(files).split()) == 0:
            pass
        elif len(str(files)) >= 0:
            # file = Relevant.write_case_relevant(files, relevant_lists)  # 是否需参数化
            file=files
            # print("type(file)",type(file))
            # print("file:",file)

    else:
        file=None

    #对ICE接口各参数判断
    def inDict(key,dict):
        if key in dict:
            return str(dict[key])
        else:
            return
    case_ip=inDict(excelVarles.case_ip,data)
    case_port=inDict(excelVarles.case_port,data)
    case_isMocl=inDict(excelVarles.case_isMocl,data)
    case_rootservice=inDict(excelVarles.case_rootservice,data)
    case_model=inDict(excelVarles.case_model,data)
    case_proxyname=inDict(excelVarles.case_proxyname,data)
    case_othmodel=inDict(excelVarles.case_othmodel,data)
    case_modelclass=inDict(excelVarles.case_modelclass,data)
    case_service=inDict(excelVarles.case_service,data)

    #断言封装
    case_subin=str(data[excelVarles.case_subin])
    case_subout=str(data[excelVarles.case_subout])
    def result_almost_assert(res):
        # assert case_subin in json.dumps(res.json(),ensure_ascii=False) #响应数据
        assert case_subin in str(res) or  case_subout not in str(res)# 响应数据

    def result_almost_asserts(res):
        case_subin_list=case_subin.strip().split(";")
        case_subout_list=case_subout.strip().split(";")
        for i in range(len(case_subin_list)):

        # assert case_subin in json.dumps(res.json(),ensure_ascii=False) #响应数据
        #     print("断言结果：",case_assert)
            # pytest.assume(case_subin_list[i] in str(res) or  case_subout not in str(res))# 响应数据
            assert case_subin_list[i] in str(res)
        for i in range(len(case_subout_list)):
            assert case_subout_list[i] not in str(res)

    #执行用例

    method=str(data[excelVarles.case_method]).upper()
    # print(method)
    url=case_ip+str(data[excelVarles.case_url])
    datas=data[excelVarles.case_data]
    case_name=str(data[excelVarles.case_name])
    case_Id=data[excelVarles.case_Id]
    logging.info("********正在执行{}**********".format(case_name))
    # print(case_name)
    if str(method):
        allure.title(case_name)
        allure.attach("接口用例请求参数:{}".format(params))
        if method=='ICE':
            # print("type(params):",type(params))
            # print("params:",params)
            res = ApiRequest().send_request(method=method,url=None,PaIsMoCl=int(case_isMocl),rootService=case_rootservice,ip=case_ip,port=case_port,model=case_model,
                                          othermodel=case_othmodel,ModelClass_name=case_modelclass,proxy_name=case_proxyname,iceservice=case_service,params=eval(params))
            r=res
        elif headers.get("Content-type")=="application/json" or  headers.get("content-type")=="application/json":
            # params=json.dumps(params)
            # print(type(params))
            # print("params是",json.loads(params))
            res=ApiRequest().send_request(method=method,url=url,json=json.loads(params),headers=headers,files=file,verify=False)
            # writeContent(r.json()['data']['access_tonken'])  # 提取出返回数据中想要的变量写入到文件中供其他接口使用
            # r=res.json()
            r = res.text
        else:
            # print("type(params)是", type(params))
            # print("params是", eval(params))
            res = ApiRequest().send_request(method=method, url=url, data=eval(params), headers=headers,files=file,verify=False)
            r = res.text

        # r=res.text
        # print("r:",r)
        get_case_relevants=Relevant.get_case_relevant(relevant, r)
        # relevant_dict_global=Relevant.get_case_relevant(relevant, r) #提取参数
        Relevant.update_Relevantdict(relevant_dict_global,get_case_relevants)#提取参数
        # print("接口提取后relevant_dict_global:", relevant_dict_global)
        relevant_lists.append(relevant_dict_global)
        # print("接口提取后relevant_lists:", relevant_lists)
        operationexcel.write_value(int(case_Id)+1,21,str(relevant_dict_global))
        # result_almost_assert(r)
        allure.dynamic.title(case_name) #报告用例名称
        result_almost_asserts(r) #根据excel预期进行断言
        return r

#1、file文件上传√
#2、ice接口 ice接口关联参数
#3、报告生成
#4、报告用例名、描述显示
if __name__ == '__main__':
    # """执行并生产allure报告"""
    # # pytest.main(["-sv","--alluredir","./report/result"])
    # pytest.main(["-s","test_api_all.py","--alluredir","../allure_report/result"])
    # pytest.main(["test_api_all.py", "--alluredir", "../allure_report/result"])
    # os.system("cd ..")
    # os.system("pytest test_pytest/ --alluredir report/result")
    # os.system("allure generate ../allure_report/result -o ../allure_report/html --clean")
    # pytest.main(["test_api_all.py","--alluredir","./allure-result/result"])
    # os.system("allure generate ./allure-result/result -o ./allure-result/html --clean")

    pytest.main(["test_allure.py","--alluredir","./allure_report/result"])
    os.system("allure generate ./allure_report/result -o ./allure_report/html --clean")
    os.system("allure open allure_report/")
    # subprocess.call("allure generate report/result/ -o report/html --clean",shell=True) #读取json文件生成html，--clean若目录存在则先清除
    # subprocess.call("allure open -h 127.0.0.1 -p 9999 ./report/html",shell=True) #生成本地服务并打开html报告
    # a={
    #     "resCode": 1,
    #     "resMessage": "success",
    #     "result": {
    #         "currentPage": 1,
    #         "items": [
    #             {
    #                 "depId": 550509,
    #                 "depName": "自动化勿动",
    #                 "displayName": "173_02",
    #                 "userId": 2594217,
    #                 "userName": "17300355552",
    #                 "userRole": 2
    #             },
    #             {
    #                 "depId": 550511,
    #                 "depName": "190_dep01",
    #                 "displayName": "173_02",
    #                 "userId": 2594233,
    #                 "userName": "17300355551",
    #                 "userRole": 2
    #             }]}}
    # print(a["result"]["items"][0]["depId"])
    #
    # import re
    # # def intMath(match) ->str:
    # #     index=match.group()
    # #     return eval(index)
    # # a1="[result][items][0][depId]"
    # # # d = re.findall(r"\d+", a)
    # # b=re.sub('\[','[\"',a1)
    # # c = re.sub('\]', '\"]', b)
    # # e=re.sub(r'\"[\d]\"',intMath, c)
    # # print(e)
    # # eee=str(a)+e
    # # print(eee)
    # # print(eval(eee))
    # value="${}"
    # r=re.findall(r"\${.+?}+", value)
    # print(r)
 #    import re,json
 #    jvalue={
 # "name":"py123_部门",
 # "verifyMode":1,
 # "departmentId":'556261',
 # "templateSetting":3}
 #    relevant_key='${depId}'
 #    relevant_name=str(556261)
 #    print(json.dumps(jvalue,ensure_ascii=False))
 #
 #    c=json.loads(json.dumps(jvalue,ensure_ascii=False))
 #    # b=str(jvalue).replace('${depId}', '556261')
 #    print(type(c))

