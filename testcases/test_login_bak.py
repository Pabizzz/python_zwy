# 开发者：Pabi
# 开发时间：2023/1/15 17:39
import pytest
import requests

from utils.read_data import get_data



class TestLogin:
    accessToken = ''
    sess = requests.session()
    csrf_token = ''
    cookie = ''



    @pytest.mark.parametrize('login', get_data['login'])
    def test_login(self, login):
        print(login)
        print(get_data['login'])
        urls = login['request']['url']
        jsons = login['request']['json']
        Header = login['request']['headers']

        res = TestLogin.sess.request("post", url=urls, data=None, json=jsons, headers=Header)
        response_post = res.json()
        TestLogin.accessToken = response_post['data']['accessToken']
        assert res.status_code == 200
        print(TestLogin.accessToken)
        print(res.status_code)




if __name__ == '__main__':
    TestLogin().test_login()

