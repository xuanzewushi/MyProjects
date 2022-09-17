# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/12 17:53
# author：彭星荣

import pytest

from conf import IOyamls, reqs


# 执行所有用例前清除cookie.yaml文件
@pytest.fixture(scope='session', autouse=True)
def clean_cookie_yaml():
    print('')
    IOyamls.clean_yaml('./animal001/test_case/cookie.yaml')
    # yield
    # IOyamls.clean_yaml('./animal001/test_case/cookie.yaml')


# 用例美化
@pytest.fixture(scope='class', autouse=False)
def class_fixture():
    print('')
    print('开始获取并写入cookie')
    yield
    print('获取cookie用例执行结束')
    print('--'*30)

# 用例美化
@pytest.fixture(scope='function', autouse=True)
def function_fixture():
    print('')
    print('开始执行测试用例')
    yield
    print('该测试用例执行结束')
    print('--'*30)