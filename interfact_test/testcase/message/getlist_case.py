import unittest
import json
# 导入自定义的文件
from base.config import *
from interface.message.my_getlist import *

# 继承自unittest库
class TestGetList(unittest.TestCase):
    def setUp(self):
        # 用自己的接口地址
        self.url = "http://sgtemplatetype/getList"

    # 第一条测试用例
    def test_getlist_case01(self):
        # 创建了一个接口对象实例
        info_inter = GetList(self.url)
        # 数据取自配置项
        header = {
            "token": token,
            "ContentType": ContentType
        }
        # 参数
        data = {
            "userType": 0
        }
        res = info_inter.iot_getlist_interface(header, data)
        code = json.loads(res.text)
        # print(code)
        # 断言
        self.assertEqual(code["msg"], "success")

    # 第二条测试用例 我这里把参数注释了  根据自己的情况设计测试用例
    def test_getlist_case02(self):
        info_inter = GetList(self.url)
        header = {
            "token": token,
            "ContentType": ContentType
        }
        data = {
            # "userType": "0"
        }
        res = info_inter.iot_getlist_interface(header, data)
        code = json.loads(res.text)
        # print(code)
        self.assertEqual(code["msg"], "success")
