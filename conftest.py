import pytest
import json
import os
from pathlib import Path

#推送推送，推送成功了吗
def pytest_addoption(parser):
    """注册自定义命令行参数 --env"""
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="指定测试环境: dev / prod / staging"
    )


@pytest.fixture(scope="session")
def env_name(request):
    """读取命令行传入的环境名称"""
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def env_config(env_name):
    """加载对应环境的配置文件"""
    config_path = Path(f"config/{env_name}_config.json")
    if not config_path.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_path}")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def env_request_data(env_name):
    """加载对应环境的请求数据"""
    data_path = Path(f"data/{env_name}_request_data.json")
    if not data_path.exists():
        return {}
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def env_response_data(env_name):
    """加载对应环境的期望响应数据"""
    data_path = Path(f"data/{env_name}_response_data.json")
    if not data_path.exists():
        return {}
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

# V1===========================================
@pytest.fixture(scope="session")
def env_config_v1(env_name):
    """加载对应环境的配置文件"""
    config_path = Path(f"config/{env_name}_config_v1.json")
    if not config_path.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_path}")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

#V1
@pytest.fixture(scope="session")
def env_request_data_v1(env_name):
    """加载对应环境的请求数据"""
    data_path = Path(f"data/v1/{env_name}_request_data.json")
    if not data_path.exists():
        return {}
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)




@pytest.fixture(scope="session")
def env_response_data_v1(env_name):
    """加载对应环境的期望响应数据"""
    data_path = Path(f"data/v1/{env_name}_response_data.json")
    if not data_path.exists():
        return {}
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)
#
# import pytest
# import json
# import os
#
#
# @pytest.fixture(scope="session")
# def env_config(request):
#     # get config file from different env
#     env = os.getenv('ENV', 'dev')
#     with open(f'config/{env}_config.json', 'r') as config_file:
#         config = json.load(config_file)
#     return config
#
#
# @pytest.fixture(scope="session")
# def env_request_data(request):
#     # get request data file from different env
#     env = os.getenv('ENV', 'dev')
#     with open(f'data/{env}_request_data.json', 'r') as request_data_file:
#         request_data = json.load(request_data_file)
#     return request_data
#
#
# @pytest.fixture (scope="session")
# def env_response_data(request):
#     # get response data file from different env
#     env = os.getenv('ENV', 'dev')
#     with open(f'data/{env}_response_data.json', 'r') as response_data_file:
#         response_data = json.load(response_data_file)
#     return response_data

