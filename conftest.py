# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/17 19:24
# author：彭星荣

import pytest
from conf import IO_yamls, my_log
import requests


# 执行用例前先获取cookie
@pytest.fixture(scope='session', autouse=True)
def login_cookie():
    # 先清除cookie.yaml的数据
    my_log.Log().info('conftest', '=='*20 + '开始执行接口自动化测试' + '=='*20)
    my_log.Log().info('conftest', '=='*20 + '清除旧的登录数据，并写入登录数据信息' + '=='*14)
    clean_message = IO_yamls.clean_yaml('case/cookie_login_case/cookie.yaml')
    my_log.Log().info('conftest', clean_message)
    print('')
    # 登录获取cookie，更新cookie.yaml的数据
    cookie_login = IO_yamls.read_yaml('case/cookie_login_case/cookie_login.yaml')
    for n in range(len(cookie_login)):
        # 获取url
        url = cookie_login[n]['url']
        # 获取请求方式
        # 获取请求数据
        params = cookie_login[n]['params']
        # 获取登录数据
        res = requests.post(url=url, params=params)
        # 写入登录数据到cookie.yaml文件
        write_message = IO_yamls.writ_yaml('case/cookie_login_case/cookie.yaml', [res.json()])
        my_log.Log().info('conftest', write_message)
    my_log.Log().info('conftest', '=='*20 + '登录数据信息写入结束' + '=='*21)
    yield
    my_log.Log().info('conftest', '=='*20 + '接口自动化测试执行结束' + '=='*20)



