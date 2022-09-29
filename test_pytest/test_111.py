# -*- coding: utf-8 -*-
"""
# @Time    :  2022/9/28 10:11
# @Author  : linxiaoyi
# @FileName: test_111.py
#@IDE ：PyCharm
"""
import pytest
from requests import models

@pytest.fixture
def make_customer_record():
    created_records = []
    def _make_customer_record(name):
        record = models.Customer(name=name, orders=[])
        created_records.append(record)
        return record
    yield _make_customer_record
    for record in created_records:
        record.destroy()
def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")

if __name__ == '__main__':
    pytest.main(["-s","test_111.py"])
