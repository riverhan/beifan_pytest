# -*- coding:utf-8 -*-
"""
# @Time : 2023/1/30 19:40
# @Author : Riveryoyo
"""
import copy
import json
import re
from string import Template

from jsonpath import jsonpath

from common.caseinfo import CaseInfo
from common.yamUtil import YamlFile


class Exchange(object):
    def __init__(self, path):
        self.file = YamlFile(path)

    def extract(self, resp, var_name, attr: str, expr: str, index=0):
        resp = copy.deepcopy(resp)
        try:
            resp.json = resp.json()
        except json.JSONDecodeError:
            resp.json = {"msg": "is not json data"}
        data = getattr(resp, attr)
        if expr.startswith('/'):
            res = None
        elif expr.startswith('$'):
            data = dict(data)
            res = jsonpath(data, expr)
        else:
            res = re.findall(expr, data)
        if res:
            value = res[index]
        else:
            value = 'not data'
        self.file[var_name] = value
        self.file.yaml_save()

    def replace(self, case_info: CaseInfo):
        case_info_str = case_info.to_yaml()
        case_info_str = Template(case_info_str).safe_substitute(self.file)
        new_case_info = case_info.by_yaml(case_info_str)
        return new_case_info


if __name__ == '__main__':
    class MockResponse:
        text = '{"name": "MockResponse", "age": 18, "data": [3, 66, 99]}'

        def json(self):
            return json.loads(self.text)


    mock_response = MockResponse()
    # print(mock_response.text)
    # print(mock_response.json_data())
    exchanger = Exchange('../extract.yaml')
    exchanger.replace()
    # 正则提取
    # exchanger.extract(mock_response, "name", "text", '"name": "(.*?)"', 0)
    # JSON提取器
    # exchanger.extract(mock_response, "name", "json", "$.name", 0)
