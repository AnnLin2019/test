# -*- coding: utf-8 -*-
"""
# @Time    :  2022/11/17 15:37
# @Author  : linxiaoyi
# @FileName: log.py
#@IDE ：PyCharm
"""
from logging import log, Logger
import logging
from common.public import File

class log:
    def __init__(self,path):
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        fp=logging.FileHandler(path,mode='a',encoding='utf-8') #创建一个Handler，用于写入日志文件
        fp.setLevel(logging.INFO)
        format=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        fp.setFormatter(format)
        self.logger.addHandler(fp)
        ch=logging.StreamHandler() #创建一个Handler用于控制台输出日志
        ch.setLevel(logging.INFO)
        ch.setFormatter(format)
        self.logger.addHandler(ch)

    def write_log(self,path):
        fp=logging.FileHandler(path,mode='a',encoding='utf-8') #创建一个Handler，用于写入日志文件
        fp.setLevel(logging.INFO)
        format=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        fp.setFormatter(format)
        self.logger.addHandler(fp)
        ch=logging.StreamHandler() #创建一个Handler用于控制台输出日志
        ch.setLevel(logging.INFO)
        ch.setFormatter(format)
        self.logger.addHandler(ch)
        # logging.basicConfig(filename=path,level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

if __name__ == '__main__':

    log_path=File().file_dir('log').joinpath('.\log.txt')
    print(log_path)
    log(log_path).write_log(log_path)
    log(log_path).logger.info("This is info message")