import os


class creatTest():

    def __init__(self):
        self.current_dir=os.path.abspath(os.path.dirname(__file__))
        self.parent_path = os.path.dirname(self.current_dir)

    def mkdir(self,testFileName,pyName):
        path=self.parent_path+'\\'+'testCase'+'\\'+testFileName
        folder = os.path.exists(path)

        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            print("------  正在创建新文件...  ------")
            print("------  目录创建成功  ------")

        else:
            print("---  文件夹已存在!  ---")


        print('**************神奇的分割线************************')


        pyPATH=path+'\\'+"test_"+""+pyName+""+".py"
        folder1=os.path.exists(pyPATH)
        if not folder1:
          f=open(pyPATH,"w")
          f.close()
          print("-------   正在创建py文件  -------")
          print("-------   py文件创建成功  -------")
        else:
            print("----  文件已存在  -----")

        fd=open(pyPATH,'w',encoding='utf-8')
        header="""from common import DB
from common import http
from common import readExcel
from common import S_Log
import unittest
import parameterized\n"""
        fd.write(header)
        config="data = readExcel.doExcel.getData('"+testFileName+"', '"+pyName+"')\n"
        fd.write(config)
        str="""httpClass = http.httpclass()
log=S_Log.LogClass()


class MyTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('***********************本次接口测试开始***********************\\n')

    @classmethod
    def tearDownClass(cls):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('***********************本次接口测试结束***********************\\n\\n\\n')



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
"""
        fd.write(str)
        fd.close()


if __name__ == '__main__':
    creatTest().mkdir('date','listHomeworkDesc3')



