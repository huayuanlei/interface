import requests
# 接口基类，封装了get和post两个方法
class BaseInterface(object):
    def __init__(self, url):
        self.url = url

    # get方法封装
    def get_methods(self, header, data):
        self.data = data
        self.header = header
        results = requests.get(url=self.url, headers=self.header, params=self.data)
        return results

    # post方法封装
    def post_methods(self, header, body):
        self.header = header
        self.body = body
        result = requests.post(url=self.url, headers=self.header, data=self.body)
        return result
