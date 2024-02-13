# 开发者：Pabi
# 开发时间：2023/3/10 17:16
import pytest

from utils.read_data import get_data
from utils.yaml_util import func_yaml


# 若yaml的数据是数组-列表-json格式，就用parametrize（多参数）
# 若yaml的数据是字典，就用get_data获取字典，data = get_data['person']
@pytest.mark.parametrize('data', get_data['person'])
def test_person(data):
    # data = get_data['person']
    print(func_yaml(data))
    # print(data)
