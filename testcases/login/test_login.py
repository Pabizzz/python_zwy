# 开发者：Pabi
# 开发时间：2024/2/13 22:12
import allure
import pytest

from api.login_api import getMobileByAccount
from utils.read import base_data


@allure.feature("登录模块")
class TestUser:
    @allure.title("验证用户合法性")
    @pytest.mark.parametrize("account_data", base_data.read_login_data()['getMobileByAccount'])
    def test_getMobileByAccount(self, account_data):
        print(account_data)
        result = getMobileByAccount(account_data)
        print(result)

