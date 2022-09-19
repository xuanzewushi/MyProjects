# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/17 18:18
# author：彭星荣

# 导包
import os

import yaml
from conf import my_log


# 读取yaml文件
def read_yaml(f_url):
    file_url = './test_case/' + f_url
    try:
        with open(file_url, 'r', encoding='utf-8') as r:
            read = yaml.load(r, Loader=yaml.FullLoader)
            return read
    except FileNotFoundError as f:
        return print(f)


# 写入yaml文件
def writ_yaml(f_url, data):
    file_url = './test_case/' + f_url
    try:
        with open(file_url, 'a', encoding='utf-8') as a:
            yaml.dump(data, a)
            return 'Successfully for write data.'
    except FileNotFoundError as f:
        return print(f)


# 清空yaml文件
def clean_yaml(f_url):
    file_url = './test_case/' + f_url
    try:
        with open(file_url, 'w', encoding='utf-8') as c:
            c.truncate()
            return 'Clean data successfully for %s.' % file_url
    except FileNotFoundError as f:
        return print(f)
