# 开发者：Pabi
# 开发时间：2022/12/29 22:48
# import re
#
# import jsonpath
import pytest
import requests

from common.requests_util import RequestUtil


# @pytest.fixture(scope="class", autouse=True)
from utils.read import base_data
from utils.read_data import get_data


# @pytest.fixture(scope="module")
# def func():
#     print('前置步骤')


# @pytest.mark.p1
class TestApi:
    # def __str__(self):
    #     return '这是海尔洗⾐机的说明书'

    # 类变量 --全局使用
    accessToken = ''
    sess = requests.session()
    csrf_token = ''
    cookie = ''

    base_url = base_data.read_ini()['host']['api_sit_url']
    # session = ''

    # def get_session(self):
    #     return requests.session()

    # def setup_class(self):
    #     print('准备测试数据')
    #
    # def teardown_class(self):
    #     print('清理测试数据')

    # def setup_method(self):
    #     print('准备测试数据')
    #
    # def teardown_method(self):
    #     print('清理测试数据')

    # 默认scop是function
    # @pytest.fixture(scope="function", autouse=True)

    # def func(self):
    #     print('前置步骤')
    #     urls = 'http://43.139.182.137:48080/admin-api/system/auth/login'
    #     return urls


    # 登录
    # @pytest.mark.p0
    @pytest.mark.parametrize('login', get_data['login'])
    def test_get_token(self, login):
        # urls = func
        # urls = 'http://43.139.182.137:48080/admin-api/system/auth/login'
        # urls = login['request'][0]
        urls = TestApi.base_url + login['request']['url']
        # urls = get_data['login']['request']['url']
        jsons = login['request']['json']
        Header = login['request']['headers']
        # jsons = {
        #     "username": "autotest",
        #     "password": "123456",
        #     "captchaVerification": "lYh5j0OEit2Qg3bo4Z0ciyqVXeUAd3Rpj0qI8yZpubEzPOVrtGrIvkYJueNnTzk9sItyPt4VzjZ9RMHbN33tnQ=="
        # }
        # Header = {
        #     "Accept": "application/json, text/plain, */*",
        #     "Accept-Encoding": "gzip, deflate",
        #     "Accept-Language": "zh-CN,zh;q=0.9",
        #     "Connection": "keep-alive",
        #     "Content-Length": "156",
        #     "Content-Type": "application/json;charset=UTF-8",
        #     "Host": "43.139.182.137:48080",
        #     "Origin": "http://43.139.182.137:48080",
        #     "Referer": "http://43.139.182.137:48080/admin-ui/login?redirect=%2Findex",
        #     "tenant-id": "1",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        # }
        # res = self.get_session().post(url=urls, data=None, json=jsons, headers=Header)
        res = TestApi.sess.request("post", url=urls, data=None, json=jsons, headers=Header)
        # res = RequestUtil().send_all_request(method="post", url=urls, data=None, json=jsons, headers=Header)
        # TestApi.cookie = res.cookies
        response_post = res.json()
        # test_1 = response_post

        # response_data = response_post['data']
        # TestApi.accessToken = response_data['accessToken']
        # TestApi.accessToken = response_post['data']['accessToken']
        TestApi.accessToken = response_post['data']['accessToken']
        # token = jsonpath.jsonpath(response_data., '$.accessToken')
        # print(res)
        # print(response_data)
        assert res.status_code == 200
        print(TestApi.accessToken)
        print(res.status_code)
        # print(TestApi.accessToken)

    # 查询接口
    # @pytest.mark.run(order=2)
    def test_select(self):
        urls = 'http://43.139.182.137:48080/admin-api/system/user/page'
        datas = {
            "pageNo": "1",
            "pageSize": "10"
        }
        Header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Authorization": "Bearer " + TestApi.accessToken,
            "Host": "43.139.182.137:48080",
            "Referer": "http://43.139.182.137:48080/admin-ui/system/user",
            "tenant-id": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        # res = requests.get(url=urls, data=datas, headers=Header)
        # res = TestApi.sess.request("get", url=urls, data=datas,  headers=Header)
        res = RequestUtil().send_all_request(method="get", url=urls, params=datas, headers=Header)
        # response_get = res.json()
        # user_data = response_get['data']['list']
        user_data = res['data']['list']
        assert res['code'] == 0
        # 断言
        # expect = xxx
        # actual = res.xxx
        # assert expect == actual
        print(user_data)

    # 编辑接口
    def test_edit(self):
        urls = 'http://43.139.182.137:48080/admin-api/system/user/update'
        jsons = {"username": "aotemane", "nickname": "1", "remark": "11111", "deptId": 101, "postIds": [], "email": "",
                 "mobile": "", "sex": 1, "avatar": "", "id": 115, "status": 0, "loginIp": "", "loginDate": "null",
                 "createTime": 1651258543000, "dept": "null", "password": ""}
        Header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Authorization": "Bearer " + TestApi.accessToken,
            "Host": "43.139.182.137:48080",
            "Referer": "http://43.139.182.137:48080/admin-ui/system/user",
            "tenant-id": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        # res = requests.put(url=urls, json=jsons, headers=Header)
        # res = TestApi.sess.request("put", url=urls, json=jsons, headers=Header)
        res = RequestUtil().send_all_request(method="put", url=urls, json=jsons, headers=Header)
        assert res['code'] == 0
        # response_get = res.json()
        # edit_data =
        print(res)

    # 文件上传
    def test_file_upload(self):
        urls = 'http://43.139.182.137:48080/admin-api/system/user/import?updateSupport=0'
        datas = {
            "file": open("C:/Users/Pabi/Downloads/用户导入模板.xls", "rb")
        }
        Header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Authorization": "Bearer " + TestApi.accessToken,
            "Host": "43.139.182.137:48080",
            "Referer": "http://43.139.182.137:48080/admin-ui/system/user",
            "tenant-id": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        # res = requests.post(url=urls, files=datas, headers=Header)
        # res = TestApi.sess.request("post", url=urls, files=datas, headers=Header)
        res = RequestUtil().send_all_request(method="post", url=urls, files=datas, headers=Header)
        assert res['code'] == 0
        # lis = jsonpath.jsonpath(res.json(), "$.accessToken")
        # response_get = res.json()
        print(res)

    # # 访问phpwind首页接口
    # def test_phpwind(self):
    #     urls = ''
    #     res = requests.get(url=urls)
    #     # 正则表达式提取
    #     TestApi().csrf_token = re.search('name="csrf_token" value="(.*?)"', res.text).group(1)
    #     print(TestApi().csrf_token)


if __name__ == '__main__':
    TestApi().test_get_token()
    TestApi().test_select()
    TestApi().test_edit()
    TestApi().test_file_upload()
