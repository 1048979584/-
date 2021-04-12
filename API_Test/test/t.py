# import json
#
# from jsonpath import jsonpath
#
# from API_Test.Get_TestCase.read_excel import ExcelUtil
# from API_Test.script.api_script import CaseScript
#
# excel = ExcelUtil("G:\LocalGit\github\QiuW\API_Test\Test_Case\ApiCase.xlsx", '调试')
# data=excel.next()[0]
# json_path=data['JsonPath']
# ReqMethod = data['请求方式']
# url2 = data['接口地址']
# Except1 = data['状态码']
# Except2 = data['响应包含']
# test_data = eval((data['参数']))
# Result01 = CaseScript().post_api(url=url2,data=test_data)
# a=Result01[1]
# # a=Result01[1].replace("null",'" "')
# # print(type(Result01[1]))
# # print(a)
# a=json.loads(a)
# print(a)
# print(type(a))
#
# # 通过jsonpath断言
# if len(json_path) != 0:
#     json_path_list = json_path.split('\n')
#     for j in json_path_list:
#         Assert_json = j.split('==')
#         json_path_result = jsonpath(a, Assert_json[0])[0]
#         print(json_path_result)
#
#
# js='''{
#     "msg":"success",
#     "code":0,
#     "data":{
#
#         "defalutCompanyType":"10",
#         "companyList":[
#             {
#                 "companyCode":"C00001",
#                 "companyName":"风策网络",
#                 "businessType":"10",
#                 "registSource":"40",
#                 "invoiceBankName":"上海银行",
#                 "companyTypeList": [
#                     {
#                         "companyCode":"C00001",
#                         "companyName":"上海风策网络科技有限公司",
#                         "companyType":"30",
#                         "companyStatus":"40",
#                         "platId":"P00001"
#                     },
#                     {
#                         "companyCode":"C00001",
#                         "companyName":"上海风策网络科技有限公司",
#                         "companyType":"10",
#                         "companyStatus":"40",
#                         "platId":"P00001"
#                     }]]
# 				}
# 			}
# }'''
#
# js=json.loads(js)
# print(type(js))
#
#
#
# a1= jsonpath(js, '$.data.companyList[0].companyTypeList[1].companyName')
# print(a1)
# # import os
# # print( os.path.abspath('ApiCase.xlsx'))
# # print( os.path.normpath('ApiCase.xlsx') )
from API_Test.Get_TestCase.read_excel import ExcelUtil
from API_Test.SQL.MysqlDB import MysqlHelper

sql_data = ExcelUtil("G:\LocalGit\github\QiuW\API_Test\Test_Case\ApiCase.xlsx", '初始化')
sql_data=sql_data.next()
for i in sql_data:
    insert_sql=i['Insert_sql']
    insert_result = MysqlHelper().insert(sql=insert_sql)
    if insert_result == 1:
        print('Insert Success  -->> %s '%(insert_sql))
    else:
        print('Insert Fail -->> %s '%(insert_sql))

sql_data2 = ExcelUtil("G:\LocalGit\github\QiuW\API_Test\Test_Case\ApiCase.xlsx", '初始化')
sql_data2 = sql_data2.next()
for j in sql_data2:
            delete_sql=j['Delete_sql']
            delete_result = MysqlHelper().delete(sql=delete_sql)
            if delete_result == 1:
                print('Delete Success  -->> %s'% (delete_sql))
            else:
                print('Delete Fail -->> %s'% (delete_sql))