# iot 我的消息  消息列表

from base.base_interface import *

class GetList(BaseInterface):
    def __init__(self, url):
        self.url = url

    def iot_getlist_interface(self, header, data):
        self.header = header
        self.data = data

        # 使用父类中的post方法
        results = self.post_methods(self.header, self.data)
        return results

