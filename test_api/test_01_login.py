# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/12 17:21
# author：彭星荣

import pytest

from conf import IOyamls, reqs, relation_yamls
import allure
import time


@allure.feature('登陆模块')
class TestLogin:

    # 成功登陆
    # @pytest.mark.usefixtures("class_fixture")
    @pytest.mark.parametrize('test_data', IOyamls.read_yaml('./animal001/test_case/t01_login.yaml'))
    @allure.story('登陆功能')
    @allure.title('用户成功正常登陆')
    def test_login_successfully_ordinary_user(self, test_data):
        url = test_data['url']
        method = test_data['method']
        params = test_data['params']
        res = reqs.RequestsMethod().request_method(method, url, params=params)
        print(res)
        IOyamls.write_yaml('./animal001/test_case/cookie.yaml', [res])
        # print('等待5s')
        # time.sleep(5)


