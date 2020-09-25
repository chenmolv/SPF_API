import configparser
import os
import  xml.dom.minidom

class readconfig:
    # 获取全部#

    def __init__(self):
        # 获取相对路径下的配置文件#
        self.current_dir = os.path.abspath(os.path.dirname(__file__))
        self.parent_path = os.path.dirname(self.current_dir)
        # self.path = self.parent_path + '\config.ini'
        self.path =None



    def Set_path(self,path):
        self.path=self.parent_path + '\\'+path
        return self.path



    #输入模块名和选项名获取对应的值,读取config.ini文件#
    def get_config_Value(self,modelName,itemName):
        if modelName==None or itemName==None:
            return
        else:
            self.cf = configparser.ConfigParser()
            self.path=readconfig().Set_path('config.ini')
            self.cf.read(self.path, 'utf-8')
            # 获取所有section，返回值为list
            secs = self.cf.sections()
            value=self.cf.get(modelName,itemName)
            return value

    # 输入模块名和选项名获取对应的值,读取run-evn.ini文件#
    def get_evn_Value(self,modelName,itemName):
        if modelName==None or itemName==None:
            return
        else:
            self.cf = configparser.ConfigParser()
            self.path=readconfig().Set_path('run-evn.ini')
            self.cf.read(self.path, 'utf-8')
            # 获取所有section，返回值为list
            secs = self.cf.sections()
            value=self.cf.get(modelName,itemName)
            return value



    def get_Xml_ModelName(self):
        dom = xml.dom.minidom.parse(self.parent_path+'\\test_Case.xml')
        # 得到文档元素对象
        root = dom.documentElement
        List=[]
        data = dom.getElementsByTagName('modelName')
        for i in range(0,len(data)):
            data2=data[i].firstChild.data
            List.append(data2)
        List=list(set(List))
        return List


    def get_Xml_testName(self):
        dom = xml.dom.minidom.parse(self.parent_path+'\\test_Case.xml')
        # 得到文档元素对象
        root = dom.documentElement
        List=[]
        data = dom.getElementsByTagName('testName')
        for i in range(0,len(data)):
            data2=data[i].firstChild.data
            List.append(data2)
        List=list(set(List))
        return List


if __name__ == "__main__":
      print(readconfig().get_Xml_testName())


