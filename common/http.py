import requests
from common import S_Log
import traceback

log=S_Log.LogClass()
class httpclass():

    def __init__(self):
        self.url=None
        self.header={}
        self.params={}
        self.timeout=10



    def set_header(self,header):
        self.header=header
        return  self.header


    def set_Params(self,params):
        # if "{token}"in params:
        #     self.params=params.replace("{token}",token)
        #
        # else:
        self.params=params
        return self.params


    def set_url(self,url):
        self.url=url
        return self.url



    def http_post(self):
        try:
            respone=requests.post(headers=self.header,url=self.url,data=self.params,timeout=10)
        except TimeoutError:
            log.log_info(traceback.print_exc())
        except AssertionError:
            log.log_info(traceback.print_exc())
        return respone

    def http_get(self):
        try:
            respone=requests.get(headers=self.header,url=self.url,params=self.params,timeout=10)
        except TimeoutError:
            print("请求超时")
            log.log_info(traceback.print_exc())
        return respone







    #
    # def getHttp(URL):
    #     response=requests.get(URL)
    #     return response
    #
    #
    # def getToken(str1):
    #  if str1 is None:
    #      return
    #  else:
    #     dic=json.loads(str1)
    #     token=dic["data"]["token"]
    #     return token
    #
    #
    #
    #
    #





















