# 开发者：Pabi
# 开发时间：2023/3/10 17:24
import random

from faker import Faker

fake = Faker(locale='zh-CN')


def random_name():
    return fake.name()


def age():
    return random.randint(10, 100)