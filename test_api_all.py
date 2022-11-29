# -*- coding: utf-8 -*-
"""
# @Time    :  2022/9/13 18:39
# @Author  : linxiaoyi
# @FileName: test_api_all.py
#@IDE ：PyCharm
"""
import pytest
import json
import allure

#参数化运行所有用例
from base.method import ApiRequest
from common import login
from common.public import File
from utils.case_assert import result_almost_asserts,result_almost_asserts_
from utils.excelVarles import excelVarles
# from utils.operationExcel import operationExcel as operationexcel
import logging
import os

from utils.operationCase import preHeader, preParam, preFile
from utils.operationSSH import Ssh2
from utils.processingRelevant import Relevant
from utils import operationExcel as op
from common.toSql import Exesql
from collections import defaultdict
from config import config
# path='F:\\Test\\Interface\\Python自动化\\git_api\\test\\data\\boss_ice_1.xlsx'
from common.toFunction import Func
from pathlib import Path
from common.log import log
# paths=File().file_path('data\\boss_api')

# operationexcel=op.operationExcel()
excels=op.Pathsexcel()
get_all_values=excels.get_all_values(config.paths)
Relevant=Relevant()
login_token=login.login_token
func = Func()
Exesql=Exesql()
log=log(config.log_path)

global relevant_dict_global, relevant_lists
relevant_dict_global = {}
relevant_lists = []
# print("全局type(relevant_dict_global)",type(relevant_dict_global))
print("当前paths：",config.paths)

def inDict(key, dict):
    if key in dict:
        return str(dict[key])
    else:
        return
def inDict2(key,dict):
    dict_n = defaultdict(str)
    dict_n.update(dict)
    return dict_n[key]

@pytest.mark.parametrize('data',get_all_values) #装饰器进行封装用例
# @allure.title(get_case_name)
# @allure.title(excel[excelVarles.case_name])
# @pytest.mark.parametrize('relevant_dict_global',relevant_dict_global) #装饰器进行封装用例
def test_api_all(data):
    print("data",data)
    global relevant_dict_global
    # relevant_dict_global = relevant_dict_global
    try:
        case_name = str(data[excelVarles.case_name])
        #动态添加模块和标题
        allure.dynamic.feature(data[excelVarles.fileName]) #feature>story>title
        allure.dynamic.story(data[excelVarles.sheetName])
        allure.dynamic.title(case_name)  # 报告用例名称
        allure.dynamic.description("请求方法是 {}，请求url是 {},请求头是 {}".format(
            data[excelVarles.case_method],data[excelVarles.case_url],data[excelVarles.case_headers]))
        # allure.dynamic.link(data[excelVarles.case_ip]+data[excelVarles.case_url]) #链接
        # allure.dynamic.issue(data[excelVarles.case_url]) #缺陷
        # allure.dynamic.testcase(data[excelVarles.case_url]) #测试用例的链接地址

        #获取是否自动化
        auto=data[excelVarles.case_isRun]
        # print("{}是否自动化{}".format(case_name,str(auto).strip().upper()))
        log.logger.info("{}是否自动化： {}".format(case_name,str(auto).strip().upper()))
        if str(auto).strip().upper() in ['NO','NONE']:
            pytest.skip("this test is skipped")

        # 获取参数关联封装
        relevant = data[excelVarles.case_relevant]

        #对请求头为空处理并添加token
        headers=data[excelVarles.case_headers]

        headers=preHeader(headers,relevant_dict_global)

        # if len(str(headers).split())==0:
        #     pass
        # elif len(str(headers))>=0:
        #     # headers['Authorization']=login_token
        #     # headers=headers
        #     # headers=Relevant.write_case_relevant(headers, relevant_lists)  # 是否需参数化
        #     headers = Relevant.write_case_relevant2(headers, relevant_dict_global)  # 是否需参数化
        #     # headers = json.loads(headers)  # 转换为字典
        #     headers = eval(headers)

        #对请求参数为空进行处理
        params=data[excelVarles.case_data]
        params=preParam(params, relevant_dict_global)
        # if len(str(params).split())==0 or params is None :
        #     # print("请求参数", params)
        #     allure.attach('None', "请求参数", attachment_type=allure.attachment_type.TEXT)
        #     pass
        # elif len(str(params))>=0:
        #     # print("请求参数",params)
        #     allure.attach(params, "请求参数", attachment_type=allure.attachment_type.TEXT)
        #     # params= Relevant.write_case_relevant(params, relevant_lists) #是否需参数化
        #
        #     params = Relevant.write_case_relevant2(params, relevant_dict_global)  # 是否需参数化
        #
        #     # params = func.replacement(params)  # 是否需要执行函数
        #     params = func.ExcuteFunction2(params)
        #     params=params.replace("'","\"")


        #对文件上传路径是否为空进行处理
        filekey=excelVarles.case_file
        file=preFile(filekey, data)
        # if excelVarles.case_file in data:
        #     files=data[excelVarles.case_file]
        #     print("files:",files)
        #     if len(str(files).split()) == 0 :
        #         pass
        #     elif files is None :
        #         file=files
        #     elif len(str(files)) >= 0:
        #         # file = Relevant.write_case_relevant(files, relevant_lists)  # 是否需参数化
        #
        #         # file=files   20221108路径优化
        #         file=func.ExcuteFunction2(files)
        #         file=file.replace("'","\"")
        #
        # else:
        #     file=None

        #对ICE接口各参数判断
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
        case_subin= Relevant.write_case_relevant2(case_subin, relevant_dict_global) # 是否需参数化
        case_subout=str(data[excelVarles.case_subout])

        #执行用例

        method=str(data[excelVarles.case_method]).upper()
        # print(method)
        #对url参数化处理
        url=case_ip+str(data[excelVarles.case_url])
        url = Relevant.write_case_relevant2(url, relevant_dict_global)  # 是否需参数化

        datas=data[excelVarles.case_data]
        case_Id=data[excelVarles.case_Id]
        # logging.info("********正在执行 {}**********".format(case_name))
        log.logger.info("********正在执行 {}**********".format(case_name))

        try:
            # print("method:",method)
            if str(method).strip(' ')=="NONE":
                try:
                    ssh = data[excelVarles.ssh]
                    if ssh:
                        allure.attach(ssh, "ssh连接信息", attachment_type=allure.attachment_type.TEXT)
                        log.logger.info("ssh连接 {}......".format(ssh))
                        Operate_ssh = Ssh2()
                        r = Operate_ssh.SshResult(str(ssh))
                except Exception as e:
                    r=str(e)
                    log.logger.error("ssh执行异常，原因：{}".format(r))
                    # print(e)
            elif str(method):
                allure.title(case_name)
                # allure.attach("接口用例请求参数:{}".format(params))
                if method=='ICE':
                    # print("type(params):",type(params))
                    # print("params:",params)
                    log.logger.info("请求方法 {}，ip {},端口 {}，接口 {}，".format(method,case_ip,case_port,case_service))
                    log.logger.info("请求参数 \n{}".format(params))
                    res = ApiRequest().send_request(method=method,url=None,PaIsMoCl=int(case_isMocl),rootService=case_rootservice,ip=case_ip,port=case_port,model=case_model,
                                                  othermodel=case_othmodel,ModelClass_name=case_modelclass,proxy_name=case_proxyname,iceservice=case_service,params=eval(params))
                    r=res
                    log.logger.info("返回\n{}".format(r))

                elif headers.get("Content-type")=="application/json" or  headers.get("content-type")=="application/json":
                    # params=json.dumps(params)
                    # print("type(params)是",type(params))
                    # print("params是",params)
                    log.logger.info("请求方法{}，\n请求头{},\n请求接口{}".format(method,headers,url))
                    log.logger.info("请求参数:\n{},\n请求文件:{}".format(params,file))
                    res=ApiRequest().send_request(method=method,url=url,json=json.loads(params),headers=headers,files=file,verify=False)
                    # writeContent(r.json()['data']['access_tonken'])  # 提取出返回数据中想要的变量写入到文件中供其他接口使用
                    # r=res.json()
                    r = res.text
                    log.logger.info("返回{}".format(r))

                else:
                    # print("type(params)是", type(params))
                    # print("params是", eval(params))
                    # print("url:",url)
                    log.logger.info("请求方法{}，请求头{},请求接口{}".format(method, headers, url))
                    log.logger.info("请求参数:\n{},\n请求文件{}".format(params, file))
                    res = ApiRequest().send_request(method=method, url=url, data=eval(params), headers=headers,files=file,verify=False)
                    r = res.text
                    log.logger.info("返回:\n {}".format(r))
                # 对ssh linux连接处理


        except TypeError:
            log.logger.info("请求方法 {}，\n请求头 {},\n请求接口 {}".format(method, headers, url))
            log.logger.info("请求参数 {},\n请求文件 {}".format(params, file))
            res = ApiRequest().send_request(method=method, url=url, data=params, headers=headers, files=file,
                                            verify=False)
            r = res.text
            log.logger.info("返回:\n {}".format(r))
        except Exception as fail:
            r='Failed : {}'.format(str(fail))
            pytest.xfail(str(fail))
            log.logger.info("请求失败，原因： {}".format(r))
        # r=res.text
        # print("r:",r)
        finally:
            get_case_relevants=Relevant.get_case_relevant(relevant, r)
            # relevant_dict_global=Relevant.get_case_relevant(relevant, r) #提取参数
            Relevant.update_Relevantdict(relevant_dict_global,get_case_relevants)#提取参数
            # print("接口提取后relevant_dict_global:", relevant_dict_global)
            relevant_lists.append(relevant_dict_global)
            # print("接口提取后relevant_lists:", relevant_lists)
            # operationexcel.write_value((int(case_Id)+1),21,str(relevant_dict_global))
            excels.write_values((int(case_Id)+1),22,str(relevant_dict_global))
            # result_almost_assert(r)
            allure.attach(method,"请求方法",attachment_type=allure.attachment_type.TEXT)
            allure.attach(url,"请求url",attachment_type=allure.attachment_type.TEXT)
            allure.attach(str(headers),"请求头",attachment_type=allure.attachment_type.TEXT)
            allure.attach(str(relevant), "提取参数", attachment_type=allure.attachment_type.TEXT)
            allure.attach(str(relevant_dict_global), "关联参数", attachment_type=allure.attachment_type.TEXT)
            allure.attach(case_subin,"断言内容",attachment_type=allure.attachment_type.TEXT) #报告显示断言
            allure.attach(str(r),"返回结果",attachment_type=allure.attachment_type.TEXT)  # 返回结果
            result_almost_asserts(case_subin, case_subout, r)  #根据excel预期进行断言

            # print("result_almost_asserts:",result_almost_asserts(case_subin, case_subout, r))  # 根据excel预期进行断言
            return r
    except KeyError as e:
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
        sql_name=inDict2(excelVarles.sql_name, data)
        auto = inDict2(excelVarles.case_isRun, data)

        # 动态添加模块和标题
        allure.dynamic.feature(data[excelVarles.fileName])  # feature>story>title
        allure.dynamic.story(data[excelVarles.sheetName])
        allure.dynamic.title(sql_name)  # 报告用例名称
        allure.title(sql_name)

        try:
            # auto = data[excelVarles.case_isRun]
            # print("{}是否自动化{}".format(sql_name, str(auto).strip().upper()))
            log.logger.info("{}是否自动化： {}".format(sql_name, str(auto).strip().upper()))
            if str(auto).strip().upper() in ['NO', 'NONE'] or not str(auto) :
                pytest.skip("this test is skipped")
            log.logger.info("连接ssh {} host {}, 执行sql语句: \n  {}......".format(ssh_address, host,sql))
            res = Exesql.execute_sql(sql, ssh_address=ssh_address, ssh_port=ssh_port, ssh_username=ssh_username,ssh_password=sshpassword,
                                     bindport=bindport, host=host,username=username, password=password, dbname=dbname,charset=charset)
            # print("执行结果：",res)
            log.logger.info("sql执行结果：{}".format(res))

            allure.dynamic.description("数据库连接信息：ssh_address {}，host {}".format(
                ssh_address, host))
            allure.attach(sql, "sql语句", attachment_type=allure.attachment_type.TEXT)
            allure.attach(str(res), "执行结果", attachment_type=allure.attachment_type.TEXT)  # 返回结果
            result_almost_asserts_('', 'Error', str(res).strip())
            # print("result_almost_asserts_:",result_almost_asserts_('', 'Error', str(res).strip()))
            # assert 'e' not in str(res).lower()

        # except Exception as ex:
        except KeyError as ex:
            # print("error:", ex)
            log.logger.error("sql执行异常，原因：{}".format(str(ex)))
            # pytest.skip("this test is skipped")
    #     except Exception as f:
    #         r='Failed : {}'.format(str(f))
    #         pytest.xfail(str(f))
    #
    # except Exception as fail:
    #     r = 'Failed : {}'.format(str(fail))
    #     pytest.xfail(str(fail))

#1、file文件上传√
#2、ice接口√ ice接口关联参数
#3、报告生成√
#4、报告用例名、描述显示√
#5、指定文件下所有excel执行用例 --
if __name__ == '__main__':
    # """执行并生产allure报告"""
    # # pytest.main(["-sv","--alluredir","./report/result"])
    # pytest.main(["-s","test_api_all.py","--alluredir","../allure_report/result"])
    # pytest.main(["test_api_all.py", "--alluredir", "../allure_report/result"])
    pytest.main(["-sv","test_api_all.py::test_api_all","--alluredir","./allure_report/result","--clean-alluredir"])
    os.system("allure generate ./allure_report/result -o ./allure_report/html --clean")
    os.system("allure open allure_report/html")

