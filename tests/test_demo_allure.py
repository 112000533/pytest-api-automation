import allure
import requests


@allure.feature("Test example API")
class TestPytestAllureDemo:

    @allure.story("Test example get endpoint")
    @allure.title("Verify the get API")
    @allure.description("verify the get API response status code and data")
    @allure.severity("blocker")
    def test_get_example_endpoint_allure(self, env_config_v1, env_request_data_v1, env_response_data_v1):
        host = env_config_v1["host"]
        get_api = env_config_v1["getAPI"]
        get_api_request_data = env_request_data_v1["getAPI"]
        get_api_response_data = env_response_data_v1["getAPI"]
        # send get request
        response = requests.get(host + get_api)
        # assert
        print("response status code is" + str(response.status_code))
        assert response.status_code == 200
        print("response data is" + str(response.json()))
        assert response.json() == get_api_response_data

    @allure.story("Test example POST API")
    @allure.title("Verify the POST API")
    @allure.description("verify the POST API response status code and data")
    @allure.severity("Critical")
    def test_post_example_endpoint_allure(self, env_config_v1, env_request_data_v1, env_response_data_v1):
        host = env_config_v1["host"]
        post_api = env_config_v1["postAPI"]
        post_api_request_data = env_request_data_v1["postAPI"]
        post_api_response_data = env_response_data_v1["postAPI"]
        # send request
        response = requests.post(host + post_api, json=post_api_request_data)
        # assert
        print("response status code is" + str(response.status_code))
        assert response.status_code == 201
        print("response data is" + str(response.json()))
        assert response.json() == post_api_response_data