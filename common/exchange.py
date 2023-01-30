# -*- coding:utf-8 -*-
"""
# @Time : 2023/1/30 19:40
# @Author : Riveryoyo
"""
from common.yamUtil import YamlFile


class Exchange(object):
    def __init__(self, path):
        self.file = YamlFile(path)

    def extract(self, resp, var_name, attr, expr, index):
        pass