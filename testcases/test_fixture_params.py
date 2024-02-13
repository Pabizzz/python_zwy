# 开发者：Pabi
# 开发时间：2023/1/10 23:45
import pytest


@pytest.fixture(params=['数据1', '数据2'], ids=['case1', 'cese2'])
def params_fixture(request):
    return request.param


def test_params(params_fixture):
    print(params_fixture)