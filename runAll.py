import unittest
import random
import time
from common import S_Log
import HTMLTestRunner
from common import readConfig
import os
import datetime
from common import mail

report_path = os.path.join(os.getcwd(), "relust")
testCase_path = os.path.join(os.getcwd(), 'testCase')
data = readConfig.readconfig().get_Xml_testName()
logger=S_Log.LogClass()


class Alltest:

    def test_setSuiteCase(self):
        print(data)
        print(testCase_path)
        test_suit = unittest.TestSuite()
        suite = []
        for case in data:
            print(case)
            discover = unittest.defaultTestLoader.discover(testCase_path, pattern=case + '.py', top_level_dir=None)
            suite.append(discover)

        for value in suite:
            test_suit.addTest(value)

        return test_suit


    def run_test(self):
        suit=self.test_setSuiteCase()
        id=str(random.randint(2000,9999))
        try:
            report_abspath = os.path.join(report_path, "result"+str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+id+".html")
            fp = open(report_abspath, "wb")
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                                          title=u'自动化测试报告,测试结果如下：',
                                                          description=u'用例执行情况：')
            runner.run(suit)
            time.sleep(10)
            mail.configMail().send("result"+str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+id)
        except Exception as ex:
            logger.log_info(ex)

     # @parameterized.parameterized.expand(data)
     # def testRun(self,modelName):
     #        path=os.path.join(os.getcwd(),'testCase\\'+str(modelName)+'')
     #        print(path)
     #        all_cases = unittest.defaultTestLoader.discover(path, pattern='l*.py')
     #        report_abspath = os.path.join(report_path, "result.html")
     #        fp = open(report_abspath, "wb")
     #        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
     #                                               title=u'自动化测试报告,测试结果如下：',
     #                                               description=u'用例执行情况：')
     #        runner.run(all_cases)
if __name__ == '__main__':
   Alltest().run_test()