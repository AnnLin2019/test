# -*- coding: utf-8 -*-
"""
# @Time    :  2022/9/29 16:15
# @Author  : linxiaoyi
# @FileName: test_333.py
#@IDE ：PyCharm
"""
import pytest
from collections import defaultdict
@pytest.fixture(scope="session")
def basemod(request):
    return pytest.importorskip("base")
@pytest.fixture(scope="session", params=["opt1", "opt2"])
def optmod(request):
    return pytest.importorskip(request.param)
def inDict2(key,dict):

    # dict_n=dict
    dict_n = defaultdict(str)
    dict_n.update(dict)
    return dict_n[key]

if __name__ == '__main__':
    key='a'
    dict={"a":1}
    print(inDict2('b',dict))

