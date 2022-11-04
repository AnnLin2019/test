import sys
import hashlib
from decimal import *
from selenium import webdriver
from time import sleep

class encrypt():
    def md5_sign(self,args):
        m=hashlib.md5()
        m.update(''.join(args))
        sign=m.hexdigest()
        return sign


if __name__ == "__main__":
    a=encrypt()
    a.md5_sign("aaaaaa")