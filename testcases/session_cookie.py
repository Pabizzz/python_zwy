# 开发者：Pabi
# 开发时间：2023/2/26 23:56

# 网页地址：http://sellshop.5istudy.online/sell/user/login_page
import requests


# def test_session_cookie():
# 新建一个会话机制，记住是Session()，大写S
req = requests.Session()

url = 'http://sellshop.5istudy.online/sell/user/login'
# url = 'http://43.139.182.137:48080/admin-api/system/auth/login'

data = {
    'username': 'test01',
    'password': '123456'
}

# data = {
#     'username': 'autotest',
#     'password': '123456'
# }

# headers = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN, zh;q = 0.9',
#     'Connection': 'keep-alive',
#     'Content-Length': '156',
#     'Content-Type': 'application/json; charset=UTF-8',
#     'Host': '43.139.182.137:48080',
#     'Origin': 'http://43.139.182.137:48080',
#     'Referer': 'http://43.139.182.137:48080/admin-ui/login?redirect=%2Findex',
#     'tenant-id': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
# }

# 登录后，req自动保存了cookie或者session
res = req.post(url=url, json=data)
# res = req.post(url=url, json=data, data=None, headers=headers)
print(res.text)
url2 = 'http://sellshop.5istudy.online/sell/seller/order/list?page=2&size=10'
# url2 = 'http://43.139.182.137:48080/admin-api/system/user/page?pageNo=1&pageSize=10&username=test_2'
res2 = req.get(url=url2)
print(res2.text)


# if __name__ == '__main__':
#     test_session_cookie()


