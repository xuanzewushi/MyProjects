# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/17 17:39
# author：彭星荣

# 导包
import os

import allure
import pytest
from conf import IO_yamls, session_class, call_log

# 所属模块
@allure.feature('登录模块')
class TestLogin:  # 定义测试类

    # 测试的接口
    @allure.story('测试登录接口：/login')
    # 定义数据驱动获取测试用例
    @pytest.mark.parametrize('t01_login', IO_yamls.read_yaml('case/test_login/t01_login.yaml'))
    # 定义测试用例
    def test_login_successfully(self, t01_login):
        # 用例名称
        case_name = t01_login['case']
        # 获取url
        url = t01_login['url']
        # 获取请求方式
        method = t01_login['method']
        # 获取请求数据
        params = t01_login['params']
        # 请求接口
        res = session_class.session_class(method=method, url=url, params=params)
        # 调用log
        call_log.call_log('test_login', t01_login, res)













