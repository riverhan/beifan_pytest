# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/15 13:33
@Author ： Riveryoyo
@IDE ：PyCharm

"""
from pathlib import Path

import platform

from common.session import Session

from common.yamUtil import YamlFile


def system_type():
    if platform.system() == 'Windows':
        case_path = Path(r'E:\PycharmProjects\beifan_pytest\yaml_data/shop_yaml')
    else:
        case_path = Path('/Users/riveryoyo/PycharmProjects/beifan_pytest/yaml_data/shop_yaml')
    return case_path


class TestApi:

    @classmethod
    def find_yaml_case(cls):
        """
        查找yaml文件
        :return:
        """
        case_path = system_type()
        print(case_path)
        yam_path_list = case_path.glob('**/test_*.yaml')
        for yaml_path in yam_path_list:
            files = YamlFile(yaml_path)
            case_func = cls.new_case(files)
            setattr(cls, f"{yaml_path.name.split('.')[0]}", case_func)

    @classmethod
    def new_case(cls, files):
        def test_func(self):
            if 'files' in files['request']:
                for k, v in files['request']['files'].items():
                    print(files['request']['files'][k])
                    files['request']['files'][k] = open(v, 'rb')
            Session().request(**files.get('request'))

        return test_func


# if __name__ == '__main__':
#     TestApi().find_yaml_case()
#     pytest.main(['-v', '-s', 'cases.py'])
TestApi().find_yaml_case()
