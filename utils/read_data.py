# 开发者：Pabi
# 开发时间：2023/1/15 0:07
import os

import yaml


path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data', 'data.yaml')

def read_data():
    f = open(path, encoding='utf-8')
    data = yaml.safe_load(f)  # 读取文件流f
    return data



get_data = read_data()
# print(get_data['login'])
# print(get_data['login']['request'])
# print(get_data['login']['request']['url'])

# if __name__ == '__main__':
#     read_data()
