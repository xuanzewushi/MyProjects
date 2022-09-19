# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/17 17:39
# author：彭星荣

# 导包
import allure
import pytest
from conf import session_class, call_log, relation_yamls

# 所属模块
@allure.feature('获取数据模块')
# 定义测试类
class TestUserData:

    # 测试的接口
    @allure.story('测试获取用户数据接口：/finduserdata')
    # 定义数据驱动获取测试用例
    @pytest.mark.parametrize('t01_user_data', relation_yamls.read_data('case/test_data/t01_user_data.yaml'))
    # 定义测试用例
    def test_login_successfully(self, t01_user_data):
        # 用例名称
        case_name = t01_user_data['case']
        # 获取url
        url = t01_user_data['url']
        # 获取请求方式
        method = t01_user_data['method']
        # 获取请求数据
        headers = t01_user_data['headers']
        # 发送请求
        res = session_class.session_class(method=method, url=url, headers=headers)
        # 调用log
        call_log.call_log('test_user_data', t01_user_data, res)
