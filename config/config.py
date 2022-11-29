# -*- coding: utf-8 -*-
"""
# @Time    :  2022/11/7 16:09
# @Author  : linxiaoyi
# @FileName: config.py
#@IDE ：PyCharm
"""
from common.public import File
import os.path
from pathlib import Path

# paths=File().file_path('data\\1')
#用例excel存放路径
testcasrpath="testcase_excel\\newboss"
#日志存放路径
log_file='.\log\log.txt'
# base_dir=os.path.abspath(os.path.pardir)
# path=os.path.join(base_dir,testcasrpath)
# base_dir=Path.cwd()
# parent_path=base_dir.parent
# path=base_dir / testcasrpath
# print("---path----",path)
paths=File().file_path(Path.cwd() / testcasrpath)
#导入用户文件存放路径
# datapath=parent_path / "data"
# print(datapath)
# paths=File().file_path(path)
# print(paths)
log_path=File().file_cwd_dir('.').joinpath(log_file)