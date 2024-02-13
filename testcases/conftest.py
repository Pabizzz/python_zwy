# 开发者：Pabi
# 开发时间：2023/1/10 22:26

# 一般用于连接数据库操作,转时间戳等等用法
import logging
from utils.log_util import logger
import pytest


@pytest.fixture(scope='session', autouse=False)
def test_session():
    print('session级别的fixture')
    a = 10
    return a


@pytest.fixture(scope='function')
def func():
    print('前置步骤清理数据')
    # urls = 'http://43.139.182.137:48080/admin-api/system/auth/login'
    yield
    print('后置步骤')
    # return urls


@pytest.fixture(scope='function')
def func_1():
    print('前置步骤清理数据')
    yield '结束'
    print('后置步骤')


@pytest.fixture(scope='function', autouse=True)
def func_log():
    # 这里使用logger是因为实例化类对象logger，utils.log_util.Logger，logger = Logger().logger
    logger.info('开始执行测试用例~')
    yield
    logger.info('测试用例执行完毕~')
