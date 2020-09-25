import  os
import xlrd
from common import  readConfig
import json


class doExcel:

     def __init__(self):
        self.current_dir = os.path.abspath(os.path.dirname(__file__))
        self.parent_path = os.path.dirname(self.current_dir)

    #需要传入文件夹的名字和Excel名字#
     def readExcel(self,fileName,excelName):
        path=self.parent_path+'\\testFile'+'\\'+fileName+'\\'+excelName+'.xls'
        excel=xlrd.open_workbook(path)
        sheet=excel.sheets()[0]
        cls=[]
        nrows=int(sheet.nrows)
        i=1
        while i<nrows:
            cls.append(sheet.row_values(i))
            i=i+1
        return cls #此处返回的是一个二维数组#


    #返回param#
     def retrunParam(list):
        x=len(list)
        i=1
        dic = {i: list[i - 1]}
        while i<=x:
            dic[i]=list[i-1][4]
            i=i+1
        return dic

    #####params中如果包含特殊的token转义，则处理，此处定义格式为：{token}  #####
     def paramsToken(params,token):
         Params=str(params)
         if '{token}'in Params:
             Params=Params.replace('{token}',token)
             return Params
         else:
             return params

     #返回预期结果#
     def retrunExcept(list):
        x=len(list)
        i=1
        dic = {i: list[i - 1]}
        while i<=x:
            dic[i]=list[i-1][5]
            i=i+1
        return dic

    #返回URL#
     def retrunUrl(list):
         x = len(list)
         i = 1
         dic = {i: list[i - 1]}
         while i <= x:
             dic[i] = list[i - 1][3]
             i = i + 1
         return dic


     def doUrl(URL):
         if(URL=="kapi"):
             url=readConfig.readconfig().get_config_Value('stable-url', 'url')
         else:
             url=URL
         return url


    #返回SQL#
     def retrunSql(list):
        x = len(list)
        i = 1
        dic = {i: list[i - 1]}
        while i <= x:
            dic[i] = list[i - 1][2]
            i = i + 1
        return dic


    ########处理sql，获取DB名和sql###
     def getDB(sql):
         if sql=="":
             return ""
         else:
          str1=str(sql)
          str2=str1.rsplit('#')
          return  str2[0]

     def getSQL(sql):
         if sql=="":
             return ""
         else:
          str1=str(sql)
          str2 = str1.rsplit('#')
          return str2[1]


     def caseName(list):
        x = len(list)
        i = 1
        dic = {i: list[i - 1]}
        while i <= x:
            dic[i] = list[i - 1][1]
            i = i + 1
        return dic


     #得到一个数据封装好的二维数组#
     def getData(fileName,excelName):
         x=doExcel().readExcel(fileName,excelName)
         lists = [[] for I in range(len(x))]
         i=1
         while i<=len(x):
             CaseName=doExcel.caseName(x)
             sql=doExcel.retrunSql(x)
             DB=doExcel.getDB(sql[i])
             SQL=doExcel.getSQL(sql[i])
             URL=doExcel.retrunUrl(x)
             PARAM=doExcel.retrunParam(x)
             EXPECT=doExcel.retrunExcept(x)
             lists[i-1]=[CaseName[i],DB,SQL,URL[i],json.loads(PARAM[i]),EXPECT[i]]
             i=i+1
         return lists


if __name__ == "__main__":
    data = doExcel.getData('date', 'listHomeworkDesc')
    print(data)







