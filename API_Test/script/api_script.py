import json
import requests
from API_Test.SQL.MysqlDB import MysqlHelper

class CaseScript:
    def __init__(self):
        #通过登陆获取token
        r=requests.get(
                url='https://test-web.wind56.com/wind56apis/auth/oauth/token',
                data={'username':'13910001000 ','password':123456},
                headers={'Content-Type':'application/json;charset=UTF-8'}).status_code
       # self.token=r.json()['expand']['token']
        self.token = r

    def get_api(self,url,params=None):
        get_status_code=requests.get(url).status_code
        get_text = requests.get(url).content.decode('utf-8')
        return get_status_code, get_text

    def post_api_session(self,url,data):
        post_result = requests.post(
            headers = {"token": self.token},
            url = url,
            data = data)
        post_status_code = post_result.status_code
        post_text = post_result.text
        return post_status_code , post_text
        #result = json.loads(r2.text)['msg']

    def post_api(self,url,data):
        post_result = requests.post(
            url = url,
            data = json.dumps(data),
            headers = {
    "content-type":"application/json;charset=UTF-8",
    "authorization":"bearer 6736b2e6-8712-46fe-992a-35673dca61ea",
    "referer":"https://test-web.wind56.com/"}
            )
        print()
        print('request_data -->>： ',data)
        print('response_data-->>： ',json.loads(post_result.content))
        return post_result.status_code , post_result.text
    def delete_api(self, url, data):
        pass
    def put_api(self, url, data):
        pass
    def var_deal(self,var_set,deal_data):
        try:
            var_dict = json.loads(var_set)
            var_dict_keys = list(var_dict.keys()) #获取所有的变量名
            for i in var_dict_keys:   #每个变量赋值
                var_value = var_dict[i]
                # var_value = MysqlHelper().get_all(sql=var_value)[0][0]
                execute_sql_result = MysqlHelper().get_all(sql=var_value)
                if execute_sql_result != 'NULL':
                    var_value = execute_sql_result[0][0]
                else:
                    var_value = execute_sql_result
                if deal_data.find(i) == -1:
                    pass
                else:
                    deal_data = deal_data.replace(i, var_value)   #替换引用变量的值
                    print("变量%s已替换为%s"%(i,var_value))
        except Exception as e:
            print(e)
        deal_data = json.loads(deal_data)
        return deal_data

    def aql_assert(self,sql_data):
        try:
            assert_sql_dict=json.loads(sql_data)
            data_dict_keys = list(assert_sql_dict.keys())
            for i in data_dict_keys:
                execute_sql = assert_sql_dict[i]
                execute_sql_result=MysqlHelper().get_all(sql=execute_sql)
                if execute_sql_result != 'NULL':
                    assert_sql_dict[i] = execute_sql_result[0][0]
                else:
                    assert_sql_dict[i] = execute_sql_result
            return assert_sql_dict
        except Exception as e:
            print(e)




if __name__ == '__main__':
    # CaseScript().get_api(url='https://www.baidu.com/')
    CaseScript().post_api(url='https://test-web.wind56.com/wind56apis/client/basClient/pageList',
                          data={
    "missionIds":"李云",
    "cancelType":"10",
    "cancelCause":"平台方操作原因",
    "cancelExplain":"委托撤销测试"
})


