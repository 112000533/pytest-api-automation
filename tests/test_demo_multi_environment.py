import requests
import json
import pytest

class TestPytestMultiEnvDemo:
    @pytest.mark.Regression  # mark the test case as regression
    def test_get_demo_multi_env(self, env_config_v1, env_request_data_v1, env_response_data_v1):
        host = env_config_v1["host"]
        get_api = env_config_v1["getAPI"]
        get_api_response_data = env_response_data_v1["getAPI"]
        # send request
        response = requests.get(host+get_api)
        # assert
        assert response.status_code == 200
        assert response.json() == get_api_response_data

    @pytest.mark.Smoke  # mark the test case as smoke
    def test_post_demo_multi_env(self, env_config_v1, env_request_data_v1, env_response_data_v1):
        host = env_config_v1["host"]
        post_api = env_config_v1["postAPI"]
        post_api_request_data = env_request_data_v1["postAPI"]
        post_api_response_data = env_response_data_v1["postAPI"]
        # send request
        response = requests.post(host + post_api,json=post_api_request_data)
        # assert
        assert response.status_code == 201
        print(response.json())
        assert response.json() == post_api_response_data

        # 语法不一样
        # $env: ENV = 'prod'; pytest tests / test_demo_multi_environment.py
