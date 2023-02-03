# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/15 13:33
@Author ： Riveryoyo
@IDE ：PyCharm

"""
from pathlib import Path

import platform

from common.caseinfo import CaseInfo
from common.exchange import Exchange
from common.session import Session

from common.yamUtil import YamlFile


def system_type():
    if platform.system() == 'Windows':
        case_path = Path(r'E:\PycharmProjects\beifan_pytest\yaml_data/shop_yaml')
    else:
        case_path = Path('/Users/riveryoyo/PycharmProjects/beifan_pytest/yaml_data/shop_yaml')
    return case_path


exchanger = Exchange('extract.yaml')


class TestApi:

    @classmethod
    def find_yaml_case(cls):
        """
        查找yaml文件
        :return:
        """
        case_path = system_type()
        yam_path_list = case_path.glob('**/test_*.yaml')
        for yaml_path in yam_path_list:
            files = YamlFile(yaml_path)
            case_info = CaseInfo(**files)
            case_func = cls.new_case(case_info)
            setattr(cls, f"{yaml_path.name.split('.')[0]}", case_func)

    @classmethod
    def new_case(cls, files):
        def test_func(self):
            new_files = exchanger.replace(files)
            if 'files' in new_files.request:
                for k, v in new_files.request['files'].items():
                    print(new_files.request['files'][k])
                    new_files.request['files'][k] = open(v, 'rb')
            result = Session().request(**new_files.request)
            print(new_files.extract)
            if new_files.extract is not None:
                for key, val in new_files.extract.items():
                    exchanger.extract(result, key, *val)

        return test_func


# if __name__ == '__main__':
#     TestApi().find_yaml_case()
#     pytest.main(['-v', '-s', 'cases.py'])
TestApi().find_yaml_case()
