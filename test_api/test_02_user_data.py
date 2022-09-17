# # !/usr/bin/python
# # -*- coding:utf-8 -*-
# # 2022/9/12 19:42
# # author：彭星荣
# import pytest
#
# from conf import reqs, relation_yamls
# import allure
#
#
# @allure.feature('用户数据模块')
# class TestUserData:
#
#     # 成功获取用户信息
#     @pytest.mark.parametrize('test_data', relation_yamls.data('./animal001/test_case/t03_user_data.yaml'))
#     @allure.story('获取用户信息页面数据功能')
#     @allure.title('成功获取用户信息')
#     def test_user_data_successfully(self, test_data):
#         url = test_data['url']
#         method = test_data['method']
#         headers = test_data['headers']
#         res = reqs.RequestsMethod().request_method(method, url, headers=headers)
#         print(res)
#
#
#
