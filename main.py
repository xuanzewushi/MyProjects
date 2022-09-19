# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/17 18:31
# author：彭星荣
import os

import pytest


if __name__ == '__main__':
    pytest.main(['-s'])
    os.system('pytest --alluredir ./reports_json --clean-alluredir')
    os.system('allure generate ./reports_json -o ./reports --clean')
