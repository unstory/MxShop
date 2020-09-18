import requests
import json
from MxShop.settings import APIKEY


class YunPian(object):
    def __init__(self, apikey):
        self.__url = "https://sms.yunpian.com/v2/sms/single_send.json"
        self.__apikey = apikey


    def send_sms(self, code, mobile):
        self.__param = {
            "apikey": self.__apikey,
            "mobile": str(mobile),
            "text": "【生鲜超市】您的验证码是：" + str(code)
        }
        response = requests.post(self.__url, data=self.__param)
        result = json.loads(response.text)
        print(result)
        return result
    
if __name__ == "__main__":
    # 初始化client,apikey作为所有请求的默认值
    yunpian = YunPian(APIKEY)
    code = 5432
    mobile = "1313xxx7774"
    yunpian.send_sms(code, mobile)
    