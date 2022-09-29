# -*- coding: utf-8 -*-
"""
# @Time    :  2022/9/21 17:05
# @Author  : linxiaoyi
# @FileName: test_report.py
#@IDE ：PyCharm
"""
import allure
import pytest
import os
from common import login
from utils.operationExcel import operationExcel
from utils.processingRelevant import Relevant

path='F:\\Test\\Interface\\Python自动化\\git_api\\test\\data\\boss_ice_1.xlsx'
operationexcel=operationExcel(path)
excel = operationexcel .get_allvalue()
login_token=login.login_token
Relevant=Relevant()
def adata():
    for i in range(1):
        yield i
@pytest.mark.parametrize('data',excel)
@allure.feature("测试用例1")
def test_case_01(data):
    print(data)
    assert data

def test_case_02():
    assert 0==0

if __name__ == '__main__':
    pytest.main(["test_report.py","--alluredir","./allure-result/result"])
    os.system("allure generate ./allure-result/result -o ./allure-result/html --clean")