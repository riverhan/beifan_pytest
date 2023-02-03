# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/15 13:18
@Author ： Riveryoyo
@IDE ：PyCharm

"""
import yaml

from common.caseinfo import CaseInfo


class YamlFile(dict):
    def __init__(self, path):
        super().__init__()
        self._path = path
        self.yaml_load()
        # self.verify_data()

    def yaml_load(self):
        with open(self._path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        if data:
            self.update(data)

    def yaml_save(self):
        with open(self._path, 'w', encoding='utf-8') as f:
            yaml.dump(dict(self), f, encoding='utf-8')


if __name__ == '__main__':
    files = YamlFile('../yaml_data/weixin_yaml/test_login.yaml')
    cases_info = CaseInfo(**files)
    a = cases_info.to_yaml()
    b = cases_info.by_yaml()
    cases_info1 = CaseInfo(**b)
    print(cases_info1)
