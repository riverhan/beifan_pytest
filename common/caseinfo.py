from dataclasses import dataclass, asdict

import yaml


@dataclass()
class CaseInfo(object):
    """
    判断实例化时是否存在name, request, extract, validate这四个属性
    """
    name: str
    request: dict
    extract: dict
    validate: dict

    def to_yaml(self) -> str:
        yaml_str = yaml.dump(asdict(self))
        return yaml_str

    @classmethod
    def by_yaml(cls, yaml_str):
        return cls(**yaml.safe_load(yaml_str))


if __name__ == '__main__':
    with open('../yaml_data/weixin_yaml/test_login.yaml') as f:
        data = yaml.safe_load(f)
    print(data)
    case_info = CaseInfo(**data)
