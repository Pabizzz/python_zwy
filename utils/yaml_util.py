# 开发者：Pabi
# 开发时间：2023/3/10 12:23
import random
from utils.func_util import random_name, age
# from faker import Faker
#
# fake = Faker(locale='zh-CN')


# 主要改动这里
def func_yaml(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if '${' and '}' in str(value):
                start = str(value).index('${')
                end = str(value).index('}')
                func_name = str(value)[start + 2:end]
                # if 'random' in str(value):
                # data[key] = str(eval(func_name))
                # data[key] = str(eval(func_name))  # 要确保eval(func_name)是str类型，不然要强转成str类型
                # data[key] = str(value)[0:start] + str(eval(func_name))  # 若前面有str字符也可以用，比如上海-${random_name()}
                data[key] = str(value)[0:start] + str(eval(func_name)) + str(value)[end+1:len(str(value))]   # 若后面有str字符也可以用，比如上海-${random_name()}-测试
    return data


# def random_name():
#     return fake.name()
#
#
# def age():
#     return random.randint(10, 100)


# if __name__ == '__main__':
#     print(random_name())
