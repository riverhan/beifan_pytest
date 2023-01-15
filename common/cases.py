# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/15 13:33
@Author ： Riveryoyo
@IDE ：PyCharm

"""
from pathlib import Path

import pytest

from common.session import Session

from common.files import YamlFile

case_path = Path('../yaml_data/shop_yaml')


class TestApi:

    @classmethod
    def find_yaml_case(cls):
        """
        查找yaml文件
        :return:
        """
        yam_path_list = case_path.glob('test_*.yaml')
        for yaml_path in yam_path_list:
            print(yaml_path.name)
            files = YamlFile(yaml_path)
            case_func = cls.new_case(files)
            print(files.get('request'))
            setattr(cls, f"{yaml_path.name}", case_func)

    @classmethod
    def new_case(cls, files):
        def test_func(self):
            response = Session().request(**files.get('request'))
            print(response.status_code)

        return test_func


# if __name__ == '__main__':
#     TestApi().find_yaml_case()
#     pytest.main(['-v', '-s', 'cases.py'])
TestApi().find_yaml_case()