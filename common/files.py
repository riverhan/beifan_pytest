# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/15 13:18
@Author ： Riveryoyo
@IDE ：PyCharm

"""
from dataclasses import dataclass

import yaml


@dataclass()
class CaseInfo(object):
    name: str
    request: dict
    extract: dict
    validate: dict


@dataclass()
class YamlFile(dict):
    def __init__(self, path):
        super().__init__()
        self._path = path
        self.yaml_load()
        self.verify_data()

    def yaml_load(self):
        with open(self._path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        if data:
            self.update(data)

    def yaml_save(self):
        with open(self._path, 'w', encoding='utf-8') as f:
            yaml.dump(dict(self), f, encoding='utf-8')

    def verify_data(self):
        CaseInfo(**self)


if __name__ == '__main__':
    files = YamlFile('../yaml_data/shop_yaml/test_login.yaml')
