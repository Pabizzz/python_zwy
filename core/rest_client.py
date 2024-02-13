# 开发者：Pabi
# 开发时间：2023/1/19 15:01

# C方法
import requests
from utils.log_util import logger
from utils.read import base_data

base_url = base_data.read_ini()['host']['api_sit_url']


class RestClient:
    def __init__(self):
        self.base_url = base_url

    # post请求有data和json
    def post(self, url, Header, jsons, **kwargs):
        # return requests.post(self.base_url + url, headers=Header, json=jsons, **kwargs)
        # return self.request("POST", url, headers=Header, json=jsons, data=None, params=None, **kwargs)
        return self.request("POST", url, headers=Header, json=jsons, data=None, params=None, **kwargs)

    # get请求有params
    def get(self, url, Header, param, **kwargs):
        # Header['Authorization'] = "Bearer " + test_case_optimize.case_optimize.TestLoginOptimize.accessToken
        return self.request("GET", url, headers=Header, data=None, json=None, params=param, **kwargs)

    # put请求有params
    def put(self, url, Header, datas, **kwargs):
        # Header['Authorization'] = "Bearer " + test_case_optimize.case_optimize.TestLoginOptimize.accessToken
        return self.request("PUT", url, headers=Header, data=datas, json=None, params=None, **kwargs)

    # delete请求,不需要data、params、json
    def delete(self, url, Header, **kwargs):
        # Header['Authorization'] = "Bearer " + test_case_optimize.case_optimize.TestLoginOptimize.accessToken
        return self.request("GET", url, headers=Header, data=None, json=None, params=None, **kwargs)

    # 封装request方法
    def request(self, method, url, headers, json, data, params, **kwargs):
        if method == "POST":
            return requests.post(url=self.base_url + url, headers=headers, json=json, data=None, params=None, **kwargs)
        if method == "GET":
            return requests.get(url=self.base_url + url, headers=headers, json=None, data=None, params=params, **kwargs)
        if method == "PUT":
            return requests.put(url=self.base_url + url, headers=headers, json=None, data=data, params=None, **kwargs)
        if method == "DELETE":
            return requests.delete(url=self.base_url + url, headers=headers, json=None, data=None, params=None, **kwargs)

    def request_log(self, method, url, headers, json, data, params, **kwargs):
        # 打印日志
        logger.info('接口请求地址>>>{}'.format(self.base_url + url))
        logger.info('接口请求方法>>>{}'.format(method))
        logger.info('接口请求头>>>{}'.format(headers))

        if json is not None:
            # \n是换行，json.dumps()是转成json格式，indent=2按照缩进格式
            logger.info('接口请求json参数>>>\n{}'.format(json.dumps(json, indent=2)))
        if data is not None:
            logger.info('接口请求data参数>>>\n{}'.format(json.dumps(data, indent=2)))
        if params is not None:
            logger.info('接口请求params参数>>>\n{}'.format(json.dumps(params, indent=2)))