import pymysql
import traceback
import re
from common import readConfig

readConfig = readConfig.readconfig()

class configDB:

    def __init__(self,DBName):
        if DBName=="":
            return
        else:
            self.DBName=DBName
            self.host=readConfig.get_config_Value(DBName, 'db_host')
            self.port=readConfig.get_config_Value(DBName, 'db_port')
            self.userName=readConfig.get_config_Value(DBName, 'db_user')
            self.password=readConfig.get_config_Value(DBName, 'db_pass')



    def connectDB(self):
        if self.host==""or self.password==""or self.port=="" or self.userName=="":
            print("输入的数据库名未匹配到，请检查sql或者配置")
        else:
            try:
                self.conn = pymysql.connect(
                 host=self.host,
                 port=int(self.port),
                 user=self.userName,
                 password=self.password,
                 database=self.DBName,
                 charset='utf8')
                self.cursor = self.conn.cursor()
            except ConnectionError as ex:
                  print(ex)
        return self.cursor



    def ExcuteSQL(self,sql):
        if sql=="":
            return
        else:
            try:
                self.connectDB()
                self.cursor.execute(sql)
                print("正在执行:"+sql)
                self.conn.commit()
                print("执行成功！")
                self.conn.close()
            except Exception as ex:
                  print(ex)




    def get_all(self, cursor):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        # 获取所有mysql执行结果
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        # 获取mysql执行完的第一条数据
        value = cursor.fetchone()
        return value






