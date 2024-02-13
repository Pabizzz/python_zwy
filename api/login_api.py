# A方法
import json

from core.api_util import api_util
from utils.log_util import logger
from utils.response_util import process_response

def login_query(param):

    response = api_util.get_login_data(params=param)
    result = process_response(response)
    return result
    # logger.info('接口返回的内容>>>:' + json.dumps(response.json()), ensure_ascii=False)
    # return response.json()


def select_query(param):
    response = api_util.get_select_data(params=param)
    result = process_response(response)
    return result


def getMobileByAccount(param):
    '''
    获得账号
    :param param:
    :return:
    '''
    account = param
    response = api_util.get_mobile_account(params=account)
    return process_response(response)


