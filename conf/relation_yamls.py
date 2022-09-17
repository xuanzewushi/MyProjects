# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/12 19:49
# author：彭星荣
import yamlinclude
from conf import IOyamls
import yaml


class Data(object):

    def __init__(self, cookie_url, data_url):
        self.cookie_url = cookie_url
        self.data_url = data_url

    # 需要关联cookie.yaml文件的普通用户的user_id
    def p_user_id(self, node):
        # time.sleep(5)
        # 调用IOyamls.read_yaml方法读取cookie.yaml文件，获取user_id
        url = self.cookie_url
        try:
            return IOyamls.read_yaml(url)[0]['user_id']
        except TypeError:
            print('还没有获取user_id')


    # 定义调用方法
    yaml.add_constructor('!p_user_id', p_user_id)


    # 需要关联cookie.yaml文件的普通用户的cookie
    def p_cookie(self, node):
        # 调用IOyamls.read_yaml方法读取cookie.yaml文件，获取cookie
        try:
            return IOyamls.read_yaml(self.cookie_url)[0]['cookie']
        except TypeError:
            print('还没有获取cookie')


    # 定义调用方法
    yaml.add_constructor('!p_cookie', p_cookie)


    # 需要关联cookie.yaml文件的admin用户的user_id
    def admin_user_id(self, node):
        # 调用IOyamls.read_yaml方法读取cookie.yaml文件，获取user_id
        try:
            return IOyamls.read_yaml(self.cookie_url)[1]['user_id']
        except TypeError:
            print('还没有获取user_id')


    # 定义调用方法
    yaml.add_constructor('!admin_user_id', admin_user_id)


    # 需要关联cookie.yaml文件的admin用户的cookie
    def admin_cookie(self, node):
        # 调用IOyamls.read_yaml方法读取cookie.yaml文件，获取cookie
        try:
            return IOyamls.read_yaml(self.cookie_url)[1]['cookie']
        except TypeError:
            print('还没有获取cookie')


    # 定义调用方法
    yaml.add_constructor('!admin_cookie', admin_cookie)


    def data(self):
        return IOyamls.read_yaml(self.data_url)


if __name__ == '__main__':
    a = Data('./animal001/test_case/cookie.yaml', './animal001/test_case/t03_user_data.yaml')
    # a = data('./animal001/test_case/cookie.yaml', './animal001/test_case/test_case/test.yaml')
    print(a.data())
