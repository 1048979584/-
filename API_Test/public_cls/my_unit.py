import os
import unittest
from API_Test.Get_TestCase.read_excel import ExcelUtil
from API_Test.SQL.MysqlDB import MysqlHelper
path = os.path.abspath('./Test_Case/ApiCase.xlsx')
class MyUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        sql_data = ExcelUtil(path, sheetName='初始化').next()
        print('### 接口测试开始 ,向数据库中加载测试数据###')
        for i in sql_data:
            insert_sql=i['Insert_sql']
            insert_result = MysqlHelper().insert(sql=insert_sql)
            if insert_result == 1:
                print('Insert Success  -->> %s'% (insert_sql))
            else:
                print('Insert Fail -->> %s'% (insert_sql))
        print('### 数据加载完成 ###')
    def setUp(self):  #测试用例之前的准备工作
        pass
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        sql_data2 = ExcelUtil(path, sheetName='初始化').next()
        print('### 接口测试结束，清理测试数据 ###')
        for j in sql_data2:
            delete_sql=j['Delete_sql']
            delete_result = MysqlHelper().delete(sql=delete_sql)
            if delete_result == 1:
                print('Delete Success  -->> %s'% (delete_sql))
            else:
                print('Delete Fail -->> %s'% (delete_sql))
        print('### 清理完成 ###')