# 开发者：Pabi
# 开发时间：2023/1/15 17:39
import allure
import pytest
import requests

from api.api import login_query, select_query
from utils.read import base_data

@allure.epic('数据进制项目epic')
@allure.feature('芋道系统模块feature')
class TestLoginOptimize:
    accessToken = ''
    sess = requests.session()
    csrf_token = ''
    cookie = ''

    base_url = base_data.read_ini()['host']['api_sit_url']

    # @pytest.mark.parametrize('login', base_data.read_data()['login'])
    # def test_read_login(self, login):

    # 登录接口
    # @allure.story('登录用例story')
    # @allure.title('测试登录功能title')
    @allure.testcase(url='/system/auth/login', name='登录接口地址testcase')
    @allure.description('autotest用户登录description')
    @allure.step('autotest用户进行登录step')
    @allure.severity('核心blocker等级severity')
    def test_read_login_optimize(self):
        '''
        登录接口
        :return:
        '''
        name = base_data.read_data()['login'][0]['name']  # 读取yaml文件的名字
        allure.dynamic.title(name)
        # allure.dynamic.story()
        param = base_data.read_data()['login']  # 读取yaml文件的数据,login的数据
        result = login_query(param)
        # 获取token
        TestLoginOptimize.accessToken = result.body['data']['accessToken']
        assert result.success is True
        assert result.body['code'] == 0

    @allure.story('查询用例story')
    @allure.title('测试查询功能title')
    @allure.testcase(url='/system/user/page ', name='查询接口地址testcase')
    @allure.description('autotest用户查询description')
    @allure.step('autotest用户进行查询step')
    @allure.severity('重要critical等级severity')
    def test_select_optimize(self):
        '''
        查询接口
        :return:
        '''
        # 写入token
        # data_token = base_data.read_data()  # 读取yaml文件的数据
        # data_token['select'][0]['request']['headers']['Authorization'] = "Bearer " + TestLoginOptimize.accessToken
        # base_data.write_data(data_token)

        param = base_data.read_data()['select']  # 读取yaml文件的数据
        result = select_query(param)
        user_data = result.body['data']['list']
        print(user_data)
        assert result.success is True
        assert result.body['code'] == 0
    # 查询接口


if __name__ == '__main__':
    TestLoginOptimize().test_read_login_optimize()
    TestLoginOptimize().test_select_optimize()
