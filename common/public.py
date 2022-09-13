# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/12 15:49
@Auth ： linxiaoyi
@File ：public.py
@IDE ：PyCharm

"""

import os
import pathlib

class File():
    def __int__(self):
        pass

    #获取指定目录
    def file_dir(self,filename):
        path = pathlib.Path(filename)
        parent_path=path.cwd().parent
        return parent_path.joinpath(filename)
    # Path(__file__).resolve().parent

    #获取某路径下的exce文件
    def file_path(self,filename):
        path=self.file_dir(filename)
        files=list(pathlib.Path(path).glob('*.xlsx'))+list(pathlib.Path(path).glob('*.xls'))
        # for file in files:
        #     print("file is {}".format(file))
        return files

if __name__ == '__main__':
    file=File()
    # print(file.file_dir('data'))
    print(file.file_path('data'))