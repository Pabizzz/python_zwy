# 开发者：Pabi
# 开发时间：2023/1/8 14:55
import requests


class RequestUtil:
    sess = requests.session()

    # 统一请求封装

    def send_all_request(self, **kwargs):
        res = RequestUtil.sess.request(**kwargs)
        response_data = res.json()
        print(response_data)
        return response_data
