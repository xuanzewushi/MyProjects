# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/19 18:22
# author：彭星荣
from conf import my_log


def call_log(log_path, file_data, res_data):
    my_log.Log().info(log_path, '==' * 20 + '用例执行结束' + '==' * 20)
    for k, v in file_data.items():
        # if v is None:
        my_log.Log().info(log_path, '{0}:{1}'.format(k, v))
    my_log.Log().info(log_path, 'Actual results：%s' % res_data)
    try:
        assert file_data['expected_result']['code'] == res_data['code']
        my_log.Log().info(log_path, '测试结果：测试通过')
        # print('测试通过')
    except AssertionError as ae:
        my_log.Log().info(log_path, '测试通过失败:%s' % ae)
        # print('测试通过失败:%s' % ae)
    my_log.Log().info(log_path, '==' * 20 + '用例执行结束' + '==' * 20)