# 开发者：Pabi
# 开发时间：2023/1/15 22:32
import configparser
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config1', 'settings.ini')

def read_ini():
    config = configparser.ConfigParser()
    config.read(path, encoding='utf8')
    return config


get_ini = read_ini()
print(read_ini()['host']['spi_sit_url'])