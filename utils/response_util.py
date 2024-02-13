# 开发者：Pabi
# 开发时间：2023/1/20 12:53
import json

from core.ResultBase import ResultResponse
from utils.log_util import logger


def process_response(response):
    if response.status_code == 200 or response.status_code == 201:
        ResultResponse.success = True
        ResultResponse.body = response.json()
        logger.info('接口返回的内容>>>:' + json.dumps(response.json(), ensure_ascii=False))
    else:
        ResultResponse.success = False
        logger.info('接口状态码不是2开头，请检查')
    return ResultResponse
