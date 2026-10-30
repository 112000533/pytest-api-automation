import requests
import json

# 数据解耦

#从配置文件获取测试配置
with open("config/config.json", "r") as f:
    config = json.load(f)
# 从测试数据文件夹获取请求数据
with open("data/request_data.json", "r") as f:
    request_data = json.load(f)
# 接口响应数据
with open("data/response_data.json", "r") as f:
    response_data = json.load(f)

class TestDemo:
    def test_get_demo(self):
        host = config.get("host")
        get_api = config.get("getAPI")
        get_api_response_data = response_data.get("getAPI")
        response = requests.get(f"{host}{get_api}")
        assert response.status_code == 200
        assert response.json() == get_api_response_data
    def test_post_demo(self):
        host = config.get("host")
        post_api = config.get("postAPI")
        post_api_request_data = request_data.get("postAPI")
        post_api_response_data = response_data.get("postAPI")
        response = requests.post(f"{host}{post_api}",json=post_api_request_data)
        assert response.status_code == 201
        assert response.json() == post_api_response_data

