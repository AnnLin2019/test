# -*- coding: utf-8 -*-
"""
# @Time    :  2022/9/29 16:15
# @Author  : linxiaoyi
# @FileName: test_333.py
#@IDE ：PyCharm
"""
import pytest
@pytest.fixture(scope="session")
def basemod(request):
return pytest.importorskip("base")
@pytest.fixture(scope="session", params=["opt1", "opt2"])
def optmod(request):
return pytest.importorskip(request.param)
