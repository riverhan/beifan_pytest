# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/15 15:53
@Author ： Riveryoyo
@IDE ：PyCharm

"""
import requests
from requests import PreparedRequest, Response
import logging

logger = logging.getLogger('debug')
logging.basicConfig(level=logging.INFO)


class Session(requests.Session):
    def __init__(self, base_url=None):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        if not url.startswith('http'):
            url = url.urljoin(self.base_url, url)
        return super().request(method, url, *args, **kwargs)

    def send(self, request: PreparedRequest, *args, **kwargs) -> Response:
        logger.info(f"发送请求>>>>>> 接口地址：{request.method}{request.url}")
        logger.info(f'发送请求>>>>>> 接口请求头：{request.headers}')
        logger.info(f'发送请求>>>>>> 接口body：{request.body}')
        response = super().send(request, *args, **kwargs)
        logger.info(f'响应请求      <<<<<< 响应状态：{response.status_code}')
        logger.info(f'响应请求      <<<<<< 响应头：{response.headers}')
        logger.info(f'响应请求      <<<<<< 响应内容：{response.content}')
        return response


