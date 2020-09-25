from common import DB
from common import http
from common import readExcel
from common import S_Log
import unittest
import parameterized
data = readExcel.doExcel.getData('date', 'listHomeworkDesc3')
httpClass = http.httpclass()
log=S_Log.LogClass()


class MyTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('***********************本次接口测试开始***********************\n')

    @classmethod
    def tearDownClass(cls):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('***********************本次接口测试结束***********************\n\n\n')



    @parameterized.parameterized.expand(data)
    def test_request(self,CaseName, db, sql, url, params, Except):
        DB.configDB(db).ExcuteSQL(sql)
        testCase=MyTest()
        self.Except=Except
        self.httpType="post"
        httpClass.set_Params(params)
        httpClass.set_url(url)
        header = {
            "version": "5.0.2",
            "User-Agent": "ios/12.1/iPhone11,8",
            "Authorization": "authorization",
            'os': 'ios'
        }
        httpClass.set_header(header)

        if self.httpType == "post":  # 根据上面配置的发送不同类型的请求#
            self.respones = httpClass.http_post()
            log.write_log(CaseName,url,params,self.respones,Except)
            testCase.check_result(self.Except, str(self.respones.json()))
        if self.httpType == "get":
            self.respones = httpClass.http_get()
            log.write_log(CaseName, url, params, self.respones, Except)
            testCase.check_result(self.Except, str(self.respones.json()))
            # self.check_relust()




    def check_result(self,Except,respones):
        if Except == "1":  # 如果用例预期填1 则必然成功#
            self.assertEquals(1, 1)
        else:
            self.assertIn(Except, respones, msg="预期和结果不一致，测试失败！！！")



if __name__ == "__main__":
    unittest.main()
