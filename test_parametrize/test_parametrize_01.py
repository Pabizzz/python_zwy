# 开发者：Pabi
# 开发时间：2023/1/14 21:28
import pytest

# # 单次循环
# # @pytest.mark.parametrize('key', value)  key是一个字符串str，values是一个列表list
# @pytest.mark.parametrize('name', ['Pabi'])
# def test_parametrize_01(name):   # 这里的key是形参，对应上面的key的名字要一样的
#     print('我是' + name)
#     assert name == 'Pabi'


# 多次循环
# 一个参数，多个值，有多少个值就执行多少次测试用例
# @pytest.mark.parametrize('key', value)  key是一个字符串str，values是一个列表list
# @pytest.mark.parametrize('hero_name', ['小乔', '黄忠', '安琪拉'])
# def test_parametrize_01(hero_name):   # 这里的key是形参，对应上面的key的名字要一样的
#     assert hero_name == '小乔'  # 用例执行三次，一次成功，两次失败


@pytest.mark.parametrize('hero', [{'name': 'Pabi姐', 'word': '好看'}, {'name': '敖老师', 'word': '可爱'}, {'name': '梅西', 'word': '太棒啦'}])
def test_parametrize_05(hero):   # 这里的key是形参，对应上面的key的名字要一样的
    print(hero['name'] + hero['word'])  # 打印name和word的值出来
    print(hero['name'])  # 打印name的值出来
    print(hero['word'])  # 打印word的值出来




if __name__ == '__main__':
    test_parametrize_05()
