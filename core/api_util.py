# 开发者：Pabi
# 开发时间：2023/1/19 14:19

# B方法,B方法接收组装好的参数（包含headers）
from core.rest_client import RestClient
import testcases.test_case_optimize.case_optimize


class Api(RestClient):
    def __init__(self):
        super().__init__()

    def get_token(self, params):
        Header = params[0]['request']['headers']
        Header['Authorization'] = "Bearer " + testcases.test_case_optimize.case_optimize.TestLoginOptimize.accessToken
        return Header

    # **kwargs是字典类型传参
    def get_login_data(self, params, **kwargs):
        # return self.post(params['request']['url'], **kwargs)
        return self.post(url=params[0]['request']['url'], Header=params[0]['request']['headers'], jsons=params[0]['request']['json'], **kwargs)

    def get_select_data(self, params, **kwargs):
        Header = self.get_token(params)
        return self.get(url=params[0]['request']['url'], Header=Header, param=params[0]['request']['params'], **kwargs)

    def get_mobile_account(self, params, **kwargs):
        # Header = self.get_token(params)
        account = params['account']
        return self.get(url='/api/identify/v8.0/users/getMobileByAccount/' + account, Header=None, param=None, **kwargs)



api_util = Api()