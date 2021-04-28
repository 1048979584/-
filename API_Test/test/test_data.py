import unittest,ddt,time,os,json,warnings
from API_Test.HwTestReport.HwTestReport import HTMLTestReport
from API_Test.Get_TestCase.read_excel import ExcelUtil
from API_Test.public_cls.my_unit import MyUnit
from API_Test.script.api_script import CaseScript
from jsonpath import jsonpath

path=os.path.abspath('./Test_Case/ApiCase.xlsx')
execute_sheet_name = ExcelUtil(path, sheetName="execute").next()[0]['execute_sheet']
excel = ExcelUtil(path,sheetName=execute_sheet_name)

@ddt.ddt
class DataTest(MyUnit):

    @ddt.data(*excel.next())

    def test_TC(self,data):
        """测试%s"""%(data['用例标题'])
        body_data = {}  # 每次遍历后将字典置为空
        ReqMethod = data['请求方式']
        url2 = data['接口地址']
        Except1 = data['状态码']
        Except2 = data['响应包含']
        json_path = data['JsonPath_Assert']
        test_data = json.loads(data['参数'])
        sql=data['Sql_Assert']
        #处理有变量的参数
        if len(data['变量设置']) != 0:
            test_data=CaseScript().var_deal(var_set=data['变量设置'],deal_data=data['参数'])
        #log打印案例信息

        print('\nCase_Item ----->>:', data['用例标题'])
        print('Request_URL --->>:', data['接口'])
        print('Request_Body -->>:', test_data)

        if ReqMethod =='get':
            Req_Result = CaseScript().get_api(url=url2,params=None)
            self.assertEqual(Except1, str(Req_Result[0]))
        # 响应文本包含关系断言
            assert_data = Except2.split('\n')
            for i in assert_data:
                self.assertIn(i, Req_Result[1])

        # 请求后通过数据库断言
            if len(sql) != 0:
                test_data = CaseScript().aql_assert(sql_data=sql)
                for j in test_data:
                    self.assertEqual(j, test_data[j])

        # 请求后通过jsonpath断言
            if len(json_path) != 0:
                json_path_dict = json.loads(json_path)
                json_path_dict = CaseScript().var_deal(var_set=data['变量设置'], deal_data=json_path)
                for k in json_path_dict:
                    json_path_result = jsonpath(json.loads(Req_Result[1]), json_path_dict[k])
                    self.assertEqual(k, json_path_result[0])


        if ReqMethod =='post_session':
            Req_Result = CaseScript().post_api_session(url=url2, data=test_data)
            self.assertEqual(Except1, str(Req_Result[0]))

            # 响应文本包含关系断言
            assert_data = Except2.split('\n')
            for i in assert_data:
                self.assertIn(i, Req_Result[1])

            # 请求后通过数据库断言
            if len(sql) != 0:
                test_data = CaseScript().aql_assert(sql_data=sql)
                for j in test_data:
                    self.assertEqual(j, test_data[j])

        # 请求后通过jsonpath断言
            if len(json_path) != 0:
                json_path_dict = json.loads(json_path)
                json_path_dict = CaseScript().var_deal(var_set=data['变量设置'], deal_data=json_path)
                for k in json_path_dict:
                    json_path_result = jsonpath(json.loads(Req_Result[1]), json_path_dict[k])
                    self.assertEqual(k, json_path_result[0])

        if ReqMethod =='post':
            Req_Result = CaseScript().post_api(url=url2,data=test_data)
            self.assertEqual(Except1, str(Req_Result[0]))

            assert_data=Except2.split('\n')
            for i in assert_data:
                self.assertIn(i,Req_Result[1])

            if len(sql) !=0:
                test_data=CaseScript().aql_assert(sql_data=sql)
                for j in test_data:
                    self.assertEqual(j,test_data[j])

            if len(json_path) != 0:
                json_path_dict = json.loads(json_path)
                json_path_dict = CaseScript().var_deal(var_set=data['变量设置'], deal_data=json_path)
                for k in json_path_dict:
                    json_path_result = jsonpath(json.loads(Req_Result[1]), json_path_dict[k])
                    if json_path_result == False:
                        json_path_result='False'
                        print('json_path_value-->>json_path 执行错误')
                    else:
                        print('json_path_value-->>:%s == %s'%(json_path_dict[k],json_path_result[0]))
                        json_path_result=json_path_result[0]
                    self.assertEqual(k , json_path_result)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
    #时间维度生成报告
    #now=time.strftime("%m_%d_%H_%M)", time.localtime())
    now = time.strftime("%Y-%m-%d)", time.localtime())
    report_name="TestReport("+now+".html"
    file_name = "G:\慧逐天下\项目接口自动化\yunzhihetong\API_Test\Test_Report\%s"%(report_name)

    with open(file_name, 'wb') as file:
        HTMLTestReport(stream=file, verbosity=3, title='接口测试报告').run(suite)





