# test
# test
序号	规 则
1	列名为红色，此列请必填。
2	headers，params无数据时，请以英文大括号“{}”代替必填。
3	报告收件人邮箱，在用例的sheet1(测试概要)中填写，可填写多个，以英文分号间隔
4	用例过多，支持使用多个页签，但请保持“测试概要”和“用例使用说明”在头尾。
5	除“用例级别,关键字,前置条件,步骤,期望结果,执行类型”6列外，其他列不可删除，但可添加。
6	
7	
8	特殊字段说明
9	checkPoint_subIn：检查点，设置存在的数据
10	checkPoint_subOut：检查点，设置不存在的数据
11	"relevant：
1）关联参数，请在需提取的用例后relevant列，按格式“${status}=[status]”设置提取的数据；
2）需提取多个参数，用英文;间隔，比如${status}=[status];${id}=[id]；
3）如果需要提取元组的值在键后英文:加下标，比如${parentId}=[result][data:0][departmentId]。"
12	params：参数中存在需关联的参数时，请在json中标出，如 "status":"${status}"，
13	PrepareSql表为预置数据，填写执行用例前需执行的sql
http	
14	"需要登录Linux机器，执行命令，需要在表单加入ssh列，并按照如下格式写入登录机器的ip、端口、账号、密码、以及执行的命令；pattern写入正则提取命令返回内容，如果无需正则提取，可不填pattern，命令返回结果依次按照out0/out1依次类推的字段名：
{'ip':'xx.xxx',
'port':xxx,
'username':'xxx',
'password':'xxxx',
'cmd':[""tac /fsmeeting/logs/dal.log |grep -E 'id .*?, target .*?, code [0-9]*$'""],
'pattern':['code (\d+)']}"
15	params，参数可以填写函数，需要正确填写模块和函数名，脚本会执行相应函数，比如{"value": "random.randint(13000000000,13999999999)"}
16	file，导入文件接口，入参需按照{"file":"F:\\Test\\Interface\\Python自动化\\project_new\\data\\员工导入部门层级xlsx"}，其中"file"为参数名，值为文件路径
ICE	
16	执行ice自动化，需要把转换后的slicepy脚本放在在main.py同级目录下，或者interface_request.py request_Ice方法，修改sys.path目录为存放slicepy脚本目录
17	执行ice自动化字段说明，PaIsMoCl:请求接口时，参数需要调用另一个模块的类的返回值作为入参则为1；直接用*args入参，则为0
	rootService:接口模块的根文件名；ip:服务器地址；port: 服务器端口；model: 被测服务根模块名；proxy_name: 代理的方法名；othermodel: 参数需要调用另一个模块时，另一个模块名（PaIsMoCl=1时需填写，否则为空）；ModelClass_name: 参数需要调用另一个模块的类，该类名（PaIsMoCl=1时需填写，否则为空）；iceservice: 被测服务名（具体）；params:被测服务参数（支持字典、数组和列表形式的入参）；varname:被测服务参数名（当入参为字典型时，需填写字典键值名）

