import pymysql
from API_Test.Get_TestCase.read_excel import ExcelUtil

class MysqlHelper(object):
    conn = None
    def __init__(self):
        excel = ExcelUtil("G:\LocalGit\github\QiuW\API_Test\Test_Case\ApiCase.xlsx", '数据库')
        connect = excel.next()[0]
        self.host = 'localhost'
        self.username = connect['username']
        self.password = connect['password']
        self.db = connect['db']
        self.charset = 'utf8'
        self.port = eval(connect['port'])

    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.username, password=self.password, db=self.db,
                            charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql, params=()):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return result

    def get_all(self, sql, params=()):
        list_data = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            list_data = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return list_data

    def insert(self, sql, params=()):
        return self.__edit(sql, params)

    def update(self, sql, params=()):
        return self.__edit(sql, params)

    def delete(self, sql, params=()):
        return self.__edit(sql, params)

    def __edit(self, sql, params):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return count
if __name__ == '__main__':

    MysqlHelper().get_all(sql="select sname from student where sid ='04';")

