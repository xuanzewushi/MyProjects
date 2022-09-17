# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/12 17:36
# author：彭星荣

import yaml


# 读取yaml文件
def read_yaml(file_url):
    # file_url = './animal001/testcase/' + url
    with open(file_url, 'r', encoding='utf-8') as r:
        read_data = yaml.load(r, Loader=yaml.FullLoader)
        return read_data


# 写入yaml文件
def write_yaml(file_url, data):
    # file_url = './animal001/testcase/' + url
    with open(file_url, 'a', encoding='utf-8') as w:
        yaml.dump(data, w)
        read = read_yaml(file_url)
        return print(read)
        # return print('Successfully for write.')


# 清除yaml文件
def clean_yaml(file_url):
    # file_url = './animal001/testcase/' + url
    with open(file_url, 'w', encoding='utf-8') as c:
        c.truncate()
        return print('Successfully for clean data.')

