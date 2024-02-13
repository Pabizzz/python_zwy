# 开发者：Pabi
# 开发时间：2023/1/14 21:56
import pytest

# 'name,word' 对应的里面['Pabi姐', '好看']也是两个值的，value可以多个值，但是形式要跟key对应。
# key有两个值，value的形式也要有两个值
# value是个列表list，也可以是[(),(),()]元组tuple()
# @pytest.mark.parametrize('name,word', [['Pabi姐', '好看'], ['敖老师', '帅气'], ['梅西', '太棒啦']])
# def test_parametrize_02(name, word):
#     print(f'{name}是{word}')
#
#
@pytest.mark.parametrize('name,word', [('Pabi姐', '好看'), ('敖老师', '帅气'), ('梅西', '太棒啦')])
def test_parametrize_03(name, word):
    print(f'{name}是{word}')

@pytest.mark.parametrize('login', [['Pabi姐', '好看'], ['敖老师', '帅气'], ['梅西', '太棒啦']])
def test_parametrize_06(login):
    print(login)
    print(login[0])

if __name__ == '__main__':
    # test_parametrize_02()
    # test_parametrize_03()
    test_parametrize_06()
