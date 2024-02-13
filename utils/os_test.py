# 开发者：Pabi
# 开发时间：2023/1/15 15:47
import os
print(os.path.relpath(__file__))  # os_test.py
print(os.path.dirname(os.path.realpath(__file__)))  # E:\PycharmProjects\python_practice\utils
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))  # E:\PycharmProjects\python_practice 主目录
print(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config1', 'data.yaml'))  # 找到主目录下的config文件的data.yaml
path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config1', 'data.yaml')
print(path)