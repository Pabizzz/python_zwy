# 开发者：Pabi
# 开发时间：2023/1/3 23:56
# import json
#
import json

import pytest


# def setup_module():
#     print('准备测试数据')
#
#
# def teardown_module():
#     print('清理测试数据')


def setup_function():
    print('准备测试数据')


def teardown_function():
    print('清理测试数据')
# def test_test():
# json_str = '{"code": 0}'
#
# # json字符串转字典
# dict_str = json.loads(json_str)
# print(dict_str)


# json转列表

# json转对象


# 用python对接口进行测试时，如果接口要求的参数是json串格式，那么在python中，需要用json.dumps()
# 方法将字典转换为json字符串;
#
# 如果接口响应结果是json字符串，在需要做断言处理时，用json.loads()
# 方法将json字符串转换为字典

# 需要用到json模块

# import json
#
# dict_var = {
#     'qwe': '123',
#     'qaz': '234'
#             }
#
# json_str = json.dumps(dict_var)
# # json_str = eval(dict_var)
#
# # dict_var2 = json.loads(json_str)
#
# print(type(json_str))  # 字典转json

# print(type(dict_var2))  # json转字典

# list_1 = ["alh", "lxq"]
# print(list_1)

# 字典
# k： str
# v:  str, list, int, bool,

@pytest.mark.skip
def test_test():
    dict_1 = {"birth": "0926", "length": ["alh", "lxq"]}
    test_1 = dict_1['length']
    print(dict_1)
    print(test_1)
# # json_1 = "{'birth': '0926', 'length': 150}"
# json_1 = '{"birth": "0926", "length": ["alh", "lxq"]}'
# print(type(json_1))
# dict_2 = json.loads(json_1)
# print(type(dict_2))
# print(dict_2)
# print(type(dict_2["length"]))

# json_list = list(json_str)
# print(json_list)
# print(type(json_list))
    tuple2 = (10, 20, ['aa', 'bb', 'cc'], 50, 30)
    print(tuple2[2])

    name_list = [['⼩明', '⼩红', '⼩绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]
    a = name_list[2][1]
    print(a)

num = '15615615611'
@pytest.mark.skipif('len(num)!=11')
def test_2():
    print(1)


if __name__ == '__main__':
    pytest.main(['q', 'test_practice.py'])
