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


# a1= jsonpath(js, '$.data.list[1].[companyCode]')
# print(a1)
import os

print( os.path.abspath('ApiCase.xlsx'))

print( os.path.normpath('ApiCase.xlsx') )