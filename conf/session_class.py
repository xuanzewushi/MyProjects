# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/17 20:28
# author：彭星荣
import requests


session = requests.session()


def session_class(method, url, **kwargs):
    method = str(method)
    if method == 'get':
        res = session.get(url=url, **kwargs)
        return res.json()
    elif method == 'post':
        res = session.post(url=url, **kwargs)
        return res.json()
    elif method == 'put':
        res = session.post(url=url, **kwargs)
        return res.json()
    else:
        pass






