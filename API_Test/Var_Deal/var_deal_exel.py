import json

import ddt
from API_Test.Get_TestCase.read_excel import ExcelUtil
from API_Test.SQL.MysqlDB import MysqlHelper
from API_Test.script.api_script import CaseScript


# class Var_Excel:
#     def __init__(self,path= 'G:\LocalGit\github\QiuW\API_Test\Test_Case\ApiCase.xlsx',sheet="调试2"):
#         self.data = ExcelUtil(path, sheet).next()
#         print(self.data )
#         self.var_dict={}
    #将变量处理成字典形式
    # def get_dict_var(self):
    #     for i in self.data:
    #         if len(i['变量']) != 0:
    #             data_dict=i['变量'].split('\n')
    #             for j in data_dict:
    #                 self.var_dict[j.split('=')[0]]=j.split('=')[1]
    #
    #
    #             print(self.var_dict)
    # def str_replace(self):
    #     data=self.data[0]['变量设置']
    #     try:
    #         if len(data) != 0:
    #             var_dict=json.loads(data)
    #             print(var_dict['@var'])
    #             var_value = MysqlHelper().get_all(sql=var_dict['@var'])[0][0]
    #             var_value=str(var_value)
    #             test_data = self.data[0]['参数'].replace('@var', var_value)
    #             test_data=json.loads(test_data)
    #             print(type(test_data))
    #             print(test_data)
    #     except Exception as e:
    #         print(e)
    #
    # CaseScript().post_api(url='https://test-web.wind56.com/wind56apis/client/basClient/pageList',
    #                       data={
    #                           "missionIds": "李云",
    #                           "cancelType": "10",
    #                           "cancelCause": "平台方操作原因",
    #                           "cancelExplain": "委托撤销测试"
    #                       })

    # Val_data=data['变量化']
    # print(Val_data)
    # Val_dict={}
    # if len(JsonPath_Val) != 0:
    #     JsonPath_Val_List = JsonPath_Val.split('\n')
    #     for i in JsonPath_Val_List:
    #         Val_list = i.split(':')
    #         print(Val_list[0])
    #         Val_dict[Val_list[0]]=Val_list[1]
    # print(Val_dict)
if __name__ == '__main__':

    path = 'G:\LocalGit\github\QiuW\API_Test\Test_Case\ApiCase.xlsx'
    sheet = "调试2"
    data = ExcelUtil(path, sheet).next()[0]


    test_data = CaseScript().aql_assert(sql_data=data['Sql_Assert'])
    print(test_data)



