# -*- coding: utf-8 -*-
"""
# @Time    :  2022/9/29 9:41
# @Author  : linxiaoyi
# @FileName: test_222.py
#@IDE ：PyCharm
"""
"""
module containing a parametrized tests testing cross-python
serialization via the pickle module.
"""
import shutil
import subprocess
import textwrap
import pytest
pythonlist = ["python3.5", "python3.6", "python3.7"]
@pytest.fixture(params=pythonlist)
def python1(request, tmp_path):
    # print("tmp_path",tmp_path)
    picklefile = tmp_path / "data.pickle"
    return Python(request.param, picklefile)

@pytest.fixture(params=pythonlist)
def python2(request, python1):
    return Python(request.param, python1.picklefile)

class Python:
    def __init__(self, version, picklefile):
        self.pythonpath = shutil.which(version)  #cmd命令 用于在PATH中找到计算机上的文件
        test1= shutil.which("python")
        print(f"pythonpath:{test1}")
        if not self.pythonpath:
            pytest.skip(f"{version!r} not found") #{!r} 输出字符串带单引号
        self.picklefile = picklefile

    def dumps(self, obj):
        dumpfile = self.picklefile.with_name("dump.py") #with_name创建一个新路径，将一个路径中的文件名替换成为另一个不同的文件名
        dumpfile.write_text(
            textwrap.dedent(
                r"""
                import pickle
                f = open({!r}, 'wb')
                s = pickle.dump({!r}, f, protocol=2)
                f.close()
                """.format(
                    str(self.picklefile), obj
                )
            )
        )
        subprocess.check_call((self.pythonpath, str(dumpfile))) #调用shell命令check_call(args, *, stdin = None, stdout = None, stderr = None, shell = False)

    def load_and_is_true(self, expression):
        loadfile = self.picklefile.with_name("load.py")
        loadfile.write_text(
            textwrap.dedent(
                r"""
                import pickle
                f = open({!r}, 'rb')
                obj = pickle.load(f)
                f.close()
                res = eval({!r})
                if not res:
                raise SystemExit(1)
                """.format(
                    str(self.picklefile), expression
                )
            )
        )
        print(loadfile)
        subprocess.check_call((self.pythonpath, str(loadfile)))

# @pytest.mark.parametrize("obj", [42, {}, {1: 3}])
# def test_basic_objects(python1, python2, obj):
#     python1.dumps(obj)
#     python2.load_and_is_true(f"obj == {obj}")

import allure
from utils.operationExcel import operationExcel
from utils.excelVarles import excelVarles
from common.public import File

# path='F:\\Test\\Interface\\Python自动化\\git_api\\test\\data\\boss_ice_1.xlsx'
# paths = File().file_path('data')



@pytest.fixture()
def get_path():
    paths = File().file_path('data')
    excels=[]
    for path in paths:
        operationexcel=operationExcel(path)
        excel = operationexcel .get_allvalue()
        fileName=File().file_name(path)
        excels.append(excel)
    return excels

@pytest.fixture()
def get_case_name(get_path):
    case_name = str(get_path[excelVarles.case_name])
    return case_name
    # return request.param

@pytest.fixture(params={"a1":1,"a2":2})
def do1(request):
    return request.param
# @pytest.mark.parametrize("name",[1,2])
# @allure.title(get_case_name)
# @allure.story("登录用例")
# @pytest.mark.parametrize('data',excel)
# def test_title(data):
#     #动态添加模块和标题
#     allure.dynamic.feature(data[excelVarles.fileName]) #feature>story>title
#     allure.dynamic.story(data[excelVarles.sheetName])
#     allure.dynamic.title(data[excelVarles.case_name])
#     # print(data[excelVarles.case_name])
#     if data[excelVarles.case_isRun]=="NO":
#         pytest.skip("this test is skipped")
#     print("执行了吗")
#
#     return data[excelVarles.case_name]

from utils import operationExcel as op
# paths=['F:\\Test\\Interface\\Python自动化\\git_api\\test\\data\\boss_ice_1.xlsx','F:\\Test\\Interface\\Python自动化\\git_api\\test\\data\\Room_1.xlsx']
paths=File().file_path('data\\2')
print("paths",paths)
# @pytest.fixture()

get_all_values=op.Pathsexcel().get_all_values(paths)
# @pytest.fixture(params=paths)
@pytest.mark.parametrize('data', get_all_values)
def test_all(data):
    allure.dynamic.feature(data[excelVarles.fileName])  # feature>story>title
    allure.dynamic.story(data[excelVarles.sheetName])
    allure.dynamic.title(data[excelVarles.case_name])
    # print(data[excelVarles.case_name])
    if data[excelVarles.case_isRun] == "NO":
        pytest.skip("this test is skipped")
    print("执行了吗")
# def test_all(request):
#         # @pytest.mark.parametrize('data', excel)
#         def a_title(data):
#             # 动态添加模块和标题
#             allure.dynamic.feature(data[excelVarles.fileName])  # feature>story>title
#             allure.dynamic.story(data[excelVarles.sheetName])
#             allure.dynamic.title(data[excelVarles.case_name])
#             # print(data[excelVarles.case_name])
#             if data[excelVarles.case_isRun] == "NO":
#                 pytest.skip("this test is skipped")
#             print("执行了吗")
#             # yield data[excelVarles.case_name]
#             # return data[excelVarles.case_name]
#         operationexcel = operationExcel(request.param)
#         excel = operationexcel.get_allvalue()
#         for data in excel:
#             print("这是excel：",data)
#             a_title(data)



if __name__ == '__main__':
    import os
    pytest.main(["-sv","test_222.py::test_all","--alluredir","./allure_report/result","--clean-alluredir"])
    os.system("allure generate ./allure_report/result -o ./allure_report/html --clean")
    os.system("allure open allure_report/html")