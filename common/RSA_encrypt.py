import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import hashlib

def crack_pwd(pwd,public_key):
    # key = """
    # -----BEGIN PUBLIC KEY-----
    # MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBALxi\/Oa\/tT5rD9BO\/fX+ND+EZOKggbl+yILFxBy8CuoQvINcr8T1Rri3xVFss1o57UDclWR4i+zwEm2bsrVfRc8CAwEAAQ==
    # -----END PUBLIC KEY-----
    # """	#注意上述key的格式
    # key="MHwwDQYJKoZIhvcNAQEBBQADawAwaAJhAI9Rso39pNE3skwWPrIndWl1h+IBTwtcgQLSF10hOS3F+DE6f5pS10IZ+OV+EOKPm+eR0wxv+5+xMKDGxj4FPGk4RF/DJMz3iFZN1GffE2jz8MVpw4KBcR9FoW4Q3KZcawIDAQAB"
    # public_key = """-----BEGIN PUBLIC KEY-----
    # MHwwDQYJKoZIhvcNAQEBBQADawAwaAJhAI9Rso39pNE3skwWPrIndWl1h+IBTwtcgQLSF10hOS3F+DE6f5pS10IZ+OV+EOKPm+eR0wxv+5+xMKDGxj4FPGk4RF/DJMz3iFZN1GffE2jz8MVpw4KBcR9FoW4Q3KZcawIDAQAB
    # -----END PUBLIC KEY-----
    # """
    public_key2="""-----BEGIN PUBLIC KEY-----
    """+public_key+"""
    -----END PUBLIC KEY-----"""
    rsakey = RSA.importKey(public_key2)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
    cipher_text = base64.b64encode(cipher.encrypt(pwd.encode(encoding="utf-8")))  # 对传递进来的用户名或密码字符串加密
    value = cipher_text.decode('utf8')  # 将加密获取到的bytes类型密文解码成str类型
    return value


def md5Encode(str):

    m = hashlib.md5()  # 创建md5对象
    # m.update(str)  # 传入需要加密的字符串进行MD5加密：
    m.update(str.encode("utf-8"))  # python3新版中字符对象是unicode对象，不能直接加密，可以改为此方式
    encodeStr = m.hexdigest()
    return encodeStr  # 获取到经过MD5加密的字符串

def saltKeymd5Encode(inputPwd,saltKey):
    pwdmd5=md5Encode(inputPwd)
    LpasswordsaltKey=pwdmd5+"{"+saltKey+"}"
    pwd=md5Encode(LpasswordsaltKey)
    return pwd

if __name__=='__main__':

    pwd = "111111"
    # public_key="""-----BEGIN PUBLIC KEY-----
    # MHwwDQYJKoZIhvcNAQEBBQADawAwaAJhAI9Rso39pNE3skwWPrIndWl1h+IBTwtcgQLSF10hOS3F+DE6f5pS10IZ+OV+EOKPm+eR0wxv+5+xMKDGxj4FPGk4RF/DJMz3iFZN1GffE2jz8MVpw4KBcR9FoW4Q3KZcawIDAQAB
    # -----END PUBLIC KEY-----
    # """
    public_key="MHwwDQYJKoZIhvcNAQEBBQADawAwaAJhAMBABZY9/uksaupvxlICeteWuq8RvVeEYZMsblX55Mp8qcdrZMcseSJLy9VOV3BhcLexE68ITfESMrOO/hmjLolDQQYMpoMdwXDK6XTxN0ujXH+WFMCo4rgCi/UADZVidwIDAQAB"
# 亲测，这种方式加密密文的长度最多只能53个数字和英文字母。  这个跟公钥有关
# 全是中文只能加密17个
    encrypted = crack_pwd(pwd,public_key)
    print(encrypted)
    funcs = "common.RSA_encrypt.crack_pwd('123456','MHwwDQYJKoZIhvcNAQEBBQADawAwaAJhAJlF0u37iq0aK1kwF+YO9xYrf2SGL8MDtYARczE8LxFt3aIOL0M1hsaKDSDXrwV5M+4F4tAz4ZVHoNWKjB1IN3Xp3KHHKaVMdqMTYQ/VhBbRkEs3y1n/j1gedeISAiYymwIDAQAB')"
