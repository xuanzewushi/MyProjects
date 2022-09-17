# # !/usr/bin/python
# # -*- coding:utf-8 -*-
# # 2022/9/12 21:47
# # author：彭星荣
# import pytest
#
# from conf import reqs, relation_yamls
# import allure
#
#
# @allure.feature('用户的动物信息模块')
# class TestAnimalData:
#
#     @pytest.mark.parametrize('test_data', relation_yamls.data('./animal001/test_case/t02_animal_data.yaml'))
#     @allure.story('获取动物信息功能')
#     @allure.title('成功获取动物信息')
#     def test_admin_animal_data(self, test_data):
#         url = test_data['url']
#         method = test_data['method']
#         params = test_data['params']
#         res = reqs.RequestsMethod().request_method(method, url, params=params)
#         print(res)
