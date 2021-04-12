import unittest,ddt,time,os,json
import warnings
from API_Test.HwTestReport.HwTestReport import HTMLTestReport
from API_Test.Get_TestCase.read_excel import ExcelUtil
from API_Test.SQL.MysqlDB import MysqlHelper
from API_Test.script.api_script import CaseScript
from jsonpath import jsonpath

excel = ExcelUtil( 'G:\LocalGit\github\QiuW\API_Test\Test_Case\ApiCase.xlsx',"案例汇总")
@ddt.ddt
class DataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # warnings.simplefilter('ignore',ResourceWarning)
        print('### 接口测试开始 ###')
        sql_data = ExcelUtil("G:\LocalGit\github\QiuW\API_Test\Test_Case\ApiCase.xlsx", '初始化')
        sql_data=sql_data.next()
        for i in sql_data:
            insert_sql=i['Insert_sql']
            insert_result = MysqlHelper().insert(sql=insert_sql)
            if insert_result == 1:
                print('Insert Success  -->> %s'% (insert_sql))
            else:
                print('Insert Fail -->> %s'% (insert_sql))
        print('### 接口测试开始 ###')
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        sql_data2 = ExcelUtil("G:\LocalGit\github\QiuW\API_Test\Test_Case\ApiCase.xlsx", '初始化')
        sql_data2 = sql_data2.next()
        for j in sql_data2:
            delete_sql=j['Delete_sql']
            delete_result = MysqlHelper().delete(sql=delete_sql)
            if delete_result == 1:
                print('Delete Success  -->> %s'% (delete_sql))
            else:
                print('Delete Fail -->> %s'% (delete_sql))
        print('### 接口测试结束 ###')

    @ddt.data(*excel.next())
    def test01(self,data):
        body_data = {}  # 每次遍历后将字典置为空
        ReqMethod = data['请求方式']
        url2 = data['接口地址']
        Except1 = data['状态码']
        Except2 = data['响应包含']
        Sql = data['Sql_Assert']
        json_path = data['JsonPath_Assert']

        if ReqMethod =='get':
            Req_Result = CaseScript().get_api(url=url2)
            self.assertEqual(Except1, str(Req_Result[0]))
            # 响应文本包含关系断言
            assert_data = Except2.split('\n')
            for i in assert_data:
                self.assertIn(i, Req_Result[1])
            # 通过数据库断言
            if len(Sql) != 0:
                Sql_list = Sql.split('\n')
                for j in Sql_list:
                    Assert_Sql_list = j.split('==')
                    sql_result = MysqlHelper().get_all(sql=Assert_Sql_list[0])
                    self.assertEqual(sql_result[0][0], Assert_Sql_list[1])
            # 通过jsonpath断言
            if len(json_path) != 0:
                json_path_list = json_path.split('\n')
                for j in json_path_list:
                    Assert_json = j.split('==')
                    json_path_result = jsonpath(json.loads(Req_Result[1]), Assert_json[0])
                    self.assertEqual(json_path_result[0], Assert_json[1])


        if ReqMethod =='post_session':
            test_data = eval((data['参数']))
            Req_Result = CaseScript().post_api_session(url=url2, data=test_data)
            self.assertEqual(Except1, str(Req_Result[0]))
            # 响应文本包含关系断言
            assert_data = Except2.split('\n')
            for i in assert_data:
                self.assertIn(i, Req_Result[1])
            # 通过数据库断言
            if len(Sql) != 0:
                Sql_list = Sql.split('\n')
                for j in Sql_list:
                    Assert_Sql_list = j.split('==')
                    sql_result = MysqlHelper().get_all(sql=Assert_Sql_list[0])
                    self.assertEqual(sql_result[0][0], Assert_Sql_list[1])
            # 通过jsonpath断言
            if len(json_path) != 0:
                json_path_list = json_path.split('\n')
                for j in json_path_list:
                    Assert_json = j.split('==')
                    json_path_result = jsonpath(json.loads(Req_Result[1]), Assert_json[0])
                    self.assertEqual(json_path_result[0], Assert_json[1])


        if ReqMethod =='post':
            test_data = eval((data['参数']))
            Req_Result = CaseScript().post_api(url=url2,data=test_data)
            self.assertEqual(Except1, str(Req_Result[0]))
            #响应文本包含关系断言
            assert_data=Except2.split('\n')
            for i in assert_data:
                self.assertIn(i,Req_Result[1])
            #通过数据库断言
            if len(Sql) != 0:
                Sql_list = Sql.split('\n')
                for j in Sql_list:
                    Assert_Sql_list=j.split('==')
                    sql_result = MysqlHelper().get_all(sql=Assert_Sql_list[0])
                    self.assertEqual(sql_result[0][0],Assert_Sql_list[1])
            #通过jsonpath断言
            if len(json_path) != 0:
                json_path_list = json_path.split('\n')
                for j in json_path_list:
                    Assert_json = j.split('==')
                    json_path_result = jsonpath(json.loads(Req_Result[1]) , Assert_json[0])
                    self.assertEqual(json_path_result[0],Assert_json[1])









if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
    #时间维度生成报告
    #now=time.strftime("%m_%d_%H_%M)", time.localtime())
    now = time.strftime("%m_%d_%H)", time.localtime())
    print(now)
    report_name="TestReport("+now+".html"
    file_name = "G:\LocalGit\github\QiuW\API_Test\Test_Report\%s"%(report_name)

    with open(file_name, 'wb') as file:
        HTMLTestReport(stream=file, verbosity=3, title='接口测试报告').run(suite)





