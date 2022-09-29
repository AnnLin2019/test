import sys, traceback, Ice,os
import com.fastonz.fmserver.companyMgr
import com.hst.boss.model
import com.hst.boss.service.common
import json
# os.chdir(os.path.split(os.path.realpath(__file__))[0])
# print(os.getcwd())
# sys.path.append('F:\Test\接口测试\ICE接口\slice2py\companyService')


status = 0
ic = None
try:
    # 初始化运行环境
    ic = Ice.initialize(sys.argv)

    # 获取远程companyService服务的代理
    base = ic.stringToProxy("commonService:default -h 47.113.118.87 -p 33001") #haoshitong环境
    #16环境192.168.5.16

    # 请求服务端确认：”这是不是 com.fastonz.fmserver.companyMgr::CompanyService的代理接口？“
    # companyService = com.fastonz.fmserver.companyMgr.CompanyServicePrx.checkedCast(base)
    commonService= com.hst.boss.service.common.CommonServicePrx.checkedCast(base)
    # print(commonService)
    # params = com.hst.boss.model.byteArray('9746653')

    model=com.hst.boss.model.Request('RecordConfig','GET',bytearray('306761',encoding='utf-8'))
    # 录制接口
    if not commonService:
        raise RuntimeError("Invalid proxy")

    # 远程调用，看起来像本地的服务一样
    by=commonService.invoke(model)
    s=by[1].result.decode('utf-8')
    js=json.loads(s)
    print(s)


    # print(by.decode('utf-8'))
    # print(commonService.invoke(model))


except:
   traceback.print_exc()
   status = 1

if ic:
   # Clean up
   try:
       ic.destroy()
   except:
       traceback.print_exc()
       status = 1

sys.exit(status)
#
#
# import sys, traceback, Ice,os
# import com.fastonz.fmserver.companyMgr
# # os.chdir(os.path.split(os.path.realpath(__file__))[0])
# # print(os.getcwd())
# # sys.path.append('F:\Test\接口测试\ICE接口\slice2py\companyService')
#
#
# status = 0
# ic = None
# try:
#     # 初始化运行环境
#     ic = Ice.initialize(sys.argv)
#
#     # 获取远程companyService服务的代理
#     base = ic.stringToProxy("companyService:default -h 192.168.7.192 -p 33001") #16环境
#
#     # 请求服务端确认：”这是不是 com.fastonz.fmserver.companyMgr::CompanyService的代理接口？“
#     companyService = com.fastonz.fmserver.companyMgr.CompanyServicePrx.checkedCast(base)
#
#     if not companyService:
#         raise RuntimeError("Invalid proxy")
#
#     # 远程调用，看起来像本地的服务一样
#
#     print(companyService.CheckOrgClosed(28))
#     print("=================================================")
#     print(companyService.GetCompanyBalance(1690515)) #电话消费，取最小整数
#     print("=================================================")
#     print(companyService.GetCompanyLicenseCount(46425, 1))
#     print("=================================================")
#     print(companyService.GetCompanyRemainCallCount(1697309))
#     print("=================================================")
#     print(companyService.GetCompanyBusiness(2))
#     print("=================================================")
#     print(companyService.GetCompanyBusiness2(4))
#     print("=================================================")
#     print(companyService.IntenalGetCompanyLicenseCount(46425, 1))
#
# except:
#    traceback.print_exc()
#    status = 1
#
# if ic:
#    # Clean up
#    try:
#        ic.destroy()
#    except:
#        traceback.print_exc()
#        status = 1
#
# sys.exit(status)