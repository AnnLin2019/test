# -*- coding: utf-8 -*-
"""
# @Time    :  2022/10/9 17:03
# @Author  : linxiaoyi
# @FileName: case_assert.py
#@IDE ：PyCharm
"""


def result_almost_assert(case_subin,case_subout,res):
    # assert case_subin in json.dumps(res.json(),ensure_ascii=False) #响应数据
    assert case_subin in str(res) or case_subout not in str(res)  # 响应数据


def result_almost_asserts_(case_subin,case_subout,res):
    # print("res:",res)
    if case_subin:
        case_subin_list = case_subin.strip().split(";")

        for i in range(len(case_subin_list)):
            # assert case_subin in json.dumps(res.json(),ensure_ascii=False) #响应数据
            #     print("断言结果：",case_assert)
            # pytest.assume(case_subin_list[i] in str(res) or  case_subout not in str(res))# 响应数据
            assert case_subin_list[i] in str(res)
    if case_subout:
        case_subout_list = case_subout.strip().split(";")
        for i in range(len(case_subout_list)):
            # print("case_subout_list",case_subout_list)
            assert case_subout_list[i] not in str(res)

def result_almost_asserts(case_subin,case_subout,res):
    case_subin_list = case_subin.strip().split(";")
    case_subout_list = case_subout.strip().split(";")
    for i in range(len(case_subin_list)):
        # assert case_subin in json.dumps(res.json(),ensure_ascii=False) #响应数据
        #     print("断言结果：",case_assert)
        # pytest.assume(case_subin_list[i] in str(res) or  case_subout not in str(res))# 响应数据
        assert case_subin_list[i] in str(res)
    for i in range(len(case_subout_list)):
        assert case_subout_list[i] not in str(res)

if __name__ == '__main__':
    r=' Error'

    print(result_almost_asserts_('','E',r))