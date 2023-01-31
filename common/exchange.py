# -*- coding:utf-8 -*-
"""
# @Time : 2023/1/30 19:40
# @Author : Riveryoyo
"""
import copy
import json
import re

from jsonpath import jsonpath

from common.yamUtil import YamlFile


class Exchange(object):
    def __init__(self, path):
        self.file = YamlFile(path)

    def extract(self, resp, var_name, attr, expr: str, index: int):
        resp = copy.deepcopy(resp)
        try:
            resp.json = resp.json_data()
        except json.JSONDecoder:
            resp.json = {"msg": "is not json data"}
        data = getattr(resp, attr)
        if expr.startswith('/'):
            res = None
        elif expr.startswith('$'):
            res = jsonpath(data, expr)
        else:
            res = re.findall(expr, data)
        if res is not None:
            value = res[index]
        else:
            value = 'not data'
        self.file[var_name] = value
        self.file.yaml_save()


if __name__ == '__main__':
    class MockResponse:
        text = '{"name": "MockResponse", "age": 18, "data": [3, 66, 99]}'

        def json_data(self):
            return json.loads(self.text)


    mock_response = MockResponse()
    print(mock_response.text)
    print(mock_response.json_data())
    exchanger = Exchange('../yaml_data/haha.yaml')
    exchanger.extract(mock_response, "name", "text", '"name": "(.*?)"', 0)
