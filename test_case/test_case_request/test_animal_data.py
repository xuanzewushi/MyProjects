# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/17 17:39
# author：彭星荣

# 导包
import pytest
from conf import session_class, call_log, relation_yamls
import allure

# 所属模块
@allure.feature('获取数据模块')
# 定义测试类
class TestAnimalData:

    # 定义数据驱动获取测试用例
    @pytest.mark.parametrize('t02_animal_data', relation_yamls.read_data('case/test_data/t02_animal_data.yaml'))
    # 测试的接口
    @allure.story('测试获取动物数据接口:/get/data')
    # 定义测试用例
    def test_login_successfully(self, t02_animal_data):
        # 用例名称
        case_name = t02_animal_data['case']
        # 获取url
        url = t02_animal_data['url']
        # 获取请求方式
        method = t02_animal_data['method']
        # 获取请求数据
        params = t02_animal_data['params']
        # 发送请求
        res = session_class.session_class(method=method, url=url, params=params)
        # 调用log
        call_log.call_log('test_animal_data', t02_animal_data, res)
