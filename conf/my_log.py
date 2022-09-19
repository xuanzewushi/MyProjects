# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/9/19 15:48
# author：彭星荣

import logging
import time
import os

log_path = os.path.join(os.path.abspath('./'), 'logs')
a = os.path.exists(log_path)
if a is False:  # 判断a路径是否存在，不存在则创建一个路径文件夹
    os.mkdir(log_path)


class Log:

    def __printconsole(self, filename, level, message):
        # 判断对应文件的log目录是否存在，不存在则创建一个路径文件夹
        file_log_path = os.path.join(os.path.abspath('./logs/'), filename)
        file_path = os.path.exists(file_log_path)
        if file_path is False:  # 判断file_path路径是否存在
            os.mkdir(file_log_path)
        # 创建一个log文件
        logname = os.path.join(file_log_path, '{0}{1} [{2}].log'.format(filename, time.strftime('%Y%m%d'), level))
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, filename, message):
        self.__printconsole(filename, 'debug', message)

    def info(self, filename,  message):
        self.__printconsole(filename, 'info', message)

    def warning(self, filename, message):
        self.__printconsole(filename, 'warning', message)

    def error(self, filename, message):
        self.__printconsole(filename, 'error', message)
