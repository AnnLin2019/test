# -*- coding: utf-8 -*-
"""
# @Time    :  2022/9/13 18:12
# @Author  : linxiaoyi
# @FileName: login.py
#@IDE ：PyCharm
"""

import pytest
import requests,json
#用户登录接口，返回token
@pytest.fixture(scope='session',autouse=True)
def login_token():
    """获取token并返回"""
    try:
        url='https://oauth.haoshitong.com/oauth2/token'
        headers={"content-type":"application/x-www-form-urlencoded","Authorization":"Basic aDUtY2xpZW50OjczNzlkYjFhLWUxNzMtNGM4ZS04OTVkLTNiNGMzOTMzOWU1OA=="}
        data={"grant_type":"password","username":"testpy@hst.com","password":"123456"}
        res=requests.post(url=url,headers=headers,data=data)
        token=str("bearer "+ res.json()['access_token'])
        return token
    except :
        print("login failed")
        return

if __name__ == '__main__':
    token=login_token()
    print(token)