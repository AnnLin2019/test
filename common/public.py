# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/12 15:49
@Auth ： linxiaoyi
@File ：public.py
@IDE ：PyCharm

"""

import os
import pathlib
import os.path
from pathlib import Path

class File():
    def __int__(self):
        pass

    #获取指定目录
    def file_dir(self,filename):
        path = pathlib.Path(filename)
        parent_path=path.cwd().parent
        return parent_path.joinpath(filename)

    def file_cwd_dir(self,filename):
        path = pathlib.Path(filename)
        parent_path=path.cwd()
        return parent_path.joinpath(filename)
    # Path(__file__).resolve().parent

    #获取某路径下的excel文件
    def file_path(self,filename):
        path=self.file_dir(filename)
        files=list(pathlib.Path(path).glob('*.xlsx'))+list(pathlib.Path(path).glob('*.xls'))
        # for file in files:
        #     print("file is {}".format(file))
        return files

    def file_all_path(self, filename):
        pass

    #获取某路径下的excel文件名
    def file_names(self,filename):
        path=self.file_dir(filename)
        # print(path)
        files=list(pathlib.Path(path).glob('*.xlsx'))+list(pathlib.Path(path).glob('*.xls'))
        file_name=[]
        for file in files:
            file_name.append(file.name)
            print("file is {}".format(file.name))
        return file_name

    def file_name(self,filepath):
        path=pathlib.Path(filepath)
        # print(path)
        return path.name



def data_path(s):
    base_dir = Path.cwd().absolute()
    parent_path = base_dir.parent
    datapath = base_dir / s
    path = '/'.join(str(datapath).split('\\'))
    # datapath=datapath.replace('\\','/')
    return path

def data_path2(s):
    base_dir = Path.cwd()
    parent_path = base_dir.parent
    datapath = parent_path / s
    return str(datapath)

def data_path3(s):
    base_dir = os.path.abspath(os.path.curdir)
    path = os.path.join(base_dir, s)
    return path


if __name__ == '__main__':
    file=File()
    path='F:\\Test\\Interface\\Python自动化\\git_api\\test\\data\\boss_ice_1.xlsx'
    # print(file.file_dir('data'))
    print(file.file_path('data'))
    print(file.file_names('data'))
    print(file.file_name(path))