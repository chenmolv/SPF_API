import logging
import os.path
import time

class LogClass():

    def __init__(self):
        self.current_dir = os.path.abspath(os.path.dirname(__file__))
        self.parent_path = os.path.dirname(self.current_dir)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)  # Log等级总开关
        # 第二步，创建一个handler，用于写入日志文件
        self.rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        self.log_path = self.parent_path + '/relust/'
        self.log_name = self.log_path + self.rq + '.log'
        self.logfile = self.log_name
        self.fh = logging.FileHandler(self.logfile, mode='w',encoding="utf-8")
        self.fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
        # 创建一个handler，用于输出到控制台
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)  # 输出到console的log等级的开关
        # 第三步，定义handler的输出格式
        self.formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        self.fh.setFormatter(self.formatter)
        # 第四步，将logger添加到handler里面
        self.logger.addHandler(self.fh)
        # 日志


    def log_info(self,msg):
        #输出到控制台
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)


        self.logger.info(msg)




    def write_log(self,CaseName,url,data,res,Except):
        self.log_info("\n\n---------------------本次用例开始------------------------")
        self.log_info("正在执行用例:"+CaseName+"\n")
        self.log_info("请求地址："+url+"\n")
        self.log_info("请求参数："+str(data)+"\n")
        self.log_info("结果："+str(res.text)+"\n")
        self.log_info("预期："+Except+"\n")
        self.log_info("\n\n---------------------本次用例结束------------------------\n\n\n\n")




if __name__ == "__main__":
  log=LogClass()
