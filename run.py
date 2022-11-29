# -*- coding: utf-8 -*-
"""
# @Time    :  2022/11/7 15:59
# @Author  : linxiaoyi
# @FileName: run.py
#@IDE ：PyCharm
"""
import allure,os
import pytest
if __name__ == '__main__':
    # """执行并生产allure报告"""

    pytest.main(["-sv","test_api_all.py::test_api_all","--alluredir","./allure_report/result","--clean-alluredir"])
    os.system("allure generate ./allure_report/result -o ./allure_report/html --clean")
    os.system("allure open allure_report/html")