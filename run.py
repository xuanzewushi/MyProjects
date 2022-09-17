# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/12 17:31
# author：彭星荣
import os

import pytest


if __name__ == '__main__':
    pytest.main(['-s', './animal001/test_api'])
    # os.system('pytest --alluredir D:/python3.8_projects/animal001/reports_json --clean-alluredir')
    # os.system('allure generate D:/python3.8_projects/animal001/reports_json -o D:/python3.8_projects/animal001/reports --clean')
