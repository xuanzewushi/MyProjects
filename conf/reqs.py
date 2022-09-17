# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/12 19:18
# author：彭星荣

import requests


class RequestsMethod:
    sess = requests.session()

    def request_method(self, method, url, **kwargs):
        method = str(method).lower()
        if method == 'get':
            res = RequestsMethod.sess.get(url, **kwargs)
            return res.json()
        elif method == 'post':
            res = RequestsMethod.sess.post(url, **kwargs)
            return res.json()
        else:
            pass

