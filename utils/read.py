# 开发者：Pabi
# 开发时间：2023/1/15 22:55
import os

import configparser
import yaml

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data', 'data.yaml')
login_data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data', 'login_data.yaml')
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config', 'settings.ini')


class FileRead:
    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path
        self.login_data_path = login_data_path

    def read_data(self):
        f = open(self.data_path, encoding='utf-8')
        data = yaml.safe_load(f)  # 读取文件流f
        return data

    # 登录数据
    def read_login_data(self):
        f = open(self.login_data_path, encoding='utf-8')
        data = yaml.safe_load(f)  # 读取文件流f
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf8')
        return config

    def write_data(self, data):
        f = open(data_path, 'w', encoding='utf-8')
        yaml.dump(data, f, allow_unicode=True)
        # with open(data_path, 'w', encoding='utf-8')as f:
        #     yaml.dump(data, f, allow_unicode=True)


base_data = FileRead()
