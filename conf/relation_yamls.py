# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/18 0:35
# author：彭星荣

import yaml

from conf import IO_yamls


def user_id(self, node):
    try:
        return IO_yamls.read_yaml('case/cookie_login_case/cookie.yaml')[1]['user_id']
    except TypeError as t:
        print('cookie.yaml文件不存在user_id')


yaml.add_constructor('!user_id', user_id)


def user_cookie(self, node):
    try:
        return IO_yamls.read_yaml('case/cookie_login_case/cookie.yaml')[1]['cookie']
    except TypeError as t:
        print('cookie.yaml文件不存在cookie')


yaml.add_constructor('!user_cookie', user_cookie)


def admin_id(self, node):
    try:
        return IO_yamls.read_yaml('case/cookie_login_case/cookie.yaml')[0]['user_id']
    except TypeError as t:
        print('cookie.yaml文件不存在user_id')


yaml.add_constructor('!admin_id', admin_id)


def admin_cookie(self, node):
    try:
        return IO_yamls.read_yaml('case/cookie_login_case/cookie.yaml')[1]['cookie']
    except TypeError as t:
        print('cookie.yaml文件不存在cookie')


yaml.add_constructor('!admin_cookie', admin_cookie)


def read_data(url):
    return IO_yamls.read_yaml(url)






