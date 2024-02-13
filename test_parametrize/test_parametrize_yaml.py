# 开发者：Pabi
# 开发时间：2023/1/14 21:56
import pytest

from utils.read_data import get_data

# 单参数
@pytest.mark.parametrize('name', get_data['heros_name'])
def test_parametrize_yaml(name):
    print(name)


# # 多参数
# @pytest.mark.parametrize('name,word', get_data['heros_name_word'])
# def test_parametrize_yaml(name, word):
#     print(f'{name}是{word}')




if __name__ == '__main__':
    test_parametrize_yaml()
