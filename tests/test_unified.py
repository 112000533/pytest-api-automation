import allure
import requests
import pytest
import json


def idfn(val):
    """自定义用例ID显示"""
    return f"{val['case_id']}-{val['name']}"


@allure.feature("API接口自动化测试")
class TestUnifiedAPI:
    """
    融合特性：
    1. Allure报告（feature/story/title/description/severity/step）
    2. 多环境支持（通过fixture读取dev/prod配置）
    3. 数据驱动（JSON外部数据）
    4. 用例分级（Smoke / Regression）
    5. 详细日志附件（请求/响应挂载到Allure报告）
    """

    # ---------- GET接口 ----------
    @allure.story("资源查询接口")
    @allure.title("GET /todos/1 - 验证查询资源成功")
    @allure.description("验证GET接口状态码200，且返回数据结构与期望一致")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.Smoke
    @pytest.mark.P0
    def test_get_todo(self, env_config, env_response_data):
        host = env_config["host"]
        api_path = env_config["apis"]["get_todo"]
        expected = env_response_data["get_todo"]

        with allure.step(f"发送GET请求: {host}{api_path}"):
            response = requests.get(f"{host}{api_path}", timeout=10)
            allure.attach(str(response.status_code), "实际状态码", allure.attachment_type.TEXT)
            allure.attach(response.text, "原始响应体", allure.attachment_type.JSON)

        with allure.step("断言：状态码是否为200"):
            assert response.status_code == 200, f"期望200，实际{response.status_code}"

        with allure.step("断言：响应体是否与期望数据一致"):
            actual = response.json()
            allure.attach(
                json.dumps(expected, ensure_ascii=False, indent=2),
                "期望数据",
                allure.attachment_type.JSON
            )
            assert actual == expected, f"响应不匹配\n期望: {expected}\n实际: {actual}"

    # ---------- POST接口 ----------
    @allure.story("资源创建接口")
    @allure.title("POST /posts - 验证创建资源成功")
    @allure.description("验证POST接口状态码201，且返回数据包含提交内容")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Regression
    @pytest.mark.P1
    def test_create_post(self, env_config, env_request_data, env_response_data):
        host = env_config["host"]
        api_path = env_config["apis"]["create_post"]
        payload = env_request_data["create_post"]
        expected = env_response_data["create_post"]

        with allure.step(f"发送POST请求: {host}{api_path}"):
            allure.attach(
                json.dumps(payload, ensure_ascii=False, indent=2),
                "请求Body",
                allure.attachment_type.JSON
            )
            response = requests.post(f"{host}{api_path}", json=payload, timeout=10)
            allure.attach(str(response.status_code), "实际状态码", allure.attachment_type.TEXT)
            allure.attach(response.text, "原始响应体", allure.attachment_type.JSON)

        with allure.step("断言：状态码是否为201"):
            assert response.status_code == 201, f"期望201，实际{response.status_code}"

        with allure.step("断言：响应体是否包含提交数据"):
            actual = response.json()
            # jsonplaceholder 会返回服务器生成的id，动态断言排除该字段
            for key in ["title", "body", "userId"]:
                assert actual.get(key) == expected.get(key), f"字段[{key}]不匹配"

    # ---------- 参数化数据驱动（进阶） ----------
    @allure.story("参数化接口验证")
    @allure.title("参数化驱动多接口验证")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.Regression
    @pytest.mark.parametrize("case_name,method,api_key,expected_status", [
        ("查询待办", "GET", "get_todo", 200),
        ("创建文章", "POST", "create_post", 201),
        ("查询文章", "GET", "get_post", 200),
    ])
    def test_api_by_parametrize(
        self, case_name, method, api_key, expected_status,
        env_config, env_request_data, env_response_data
    ):
        """使用pytest.mark.parametrize实现真正的数据驱动"""
        host = env_config["host"]
        api_path = env_config["apis"][api_key]

        with allure.step(f"【{case_name}】发送 {method} 请求"):
            if method == "GET":
                response = requests.get(f"{host}{api_path}", timeout=10)
            else:
                payload = env_request_data.get(api_key, {})
                response = requests.post(f"{host}{api_path}", json=payload, timeout=10)

            allure.attach(str(response.status_code), "状态码", allure.attachment_type.TEXT)
            allure.attach(response.text, "响应", allure.attachment_type.JSON)

        with allure.step(f"断言状态码为 {expected_status}"):
            assert response.status_code == expected_status

    # ---------- PUT接口 ----------
    @allure.story("资源更新接口")
    @allure.title("PUT /posts/1 - 验证更新资源成功")
    @allure.description("验证PUT接口状态码200，且返回数据包含更新内容")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Regression
    @pytest.mark.P1
    def test_update_post(self, env_config, env_request_data, env_response_data):
        host = env_config["host"]
        api_path = env_config["apis"]["update_post"]
        payload = env_request_data["update_post"]
        expected = env_response_data["update_post"]

        with allure.step(f"发送PUT请求: {host}{api_path}"):
            allure.attach(
                json.dumps(payload, ensure_ascii=False, indent=2),
                "请求Body", allure.attachment_type.JSON
            )
            response = requests.put(f"{host}{api_path}", json=payload, timeout=10)
            allure.attach(str(response.status_code), "实际状态码", allure.attachment_type.TEXT)
            allure.attach(response.text, "原始响应体", allure.attachment_type.JSON)

        with allure.step("断言：状态码是否为200"):
            assert response.status_code == 200, f"期望200，实际{response.status_code}"

        with allure.step("断言：响应体是否包含更新数据"):
            actual = response.json()
            for key in ["title", "body", "userId"]:
                assert actual.get(key) == expected.get(key), f"字段[{key}]不匹配"
