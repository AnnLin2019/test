# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/12 15:41
@Auth ： linxiaoyi
@File ：method.py
@IDE ：PyCharm

"""

import requests
import json

class ApiRequest(object):
    def __init__(self):
        pass
    def send_request(self,method,url,data=None,params=None,headers=None,cookies=None,json=None,files=None,auth=None,timeout=None,proxies=None,verify=None,cert=None):
        self.res=requests.request(method=method,url=url,data=data,params=params,headers=headers,cookies=cookies,json=json,files=files,auth=auth,timeout=timeout,proxies=proxies,verify=verify,cert=cert)
        return self.res


