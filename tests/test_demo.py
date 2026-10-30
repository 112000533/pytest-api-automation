import requests

# 基础接口请求+assert断言
class TestPytestDemo:
    def test_get_demo(self):
        base_url = "https://jsonplaceholder.typicode.com"  # 假数据请求网站 json place holder
        response = requests.get(f"{base_url}/todos/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1
        assert response.json()["title"] == "delectus aut autem"
    def test_post_demo(self):
        base_url = "https://jsonplaceholder.typicode.com"
        payload = {"title": "foo", "body": "bar", "userId": 1}
        response = requests.post(f"{base_url}/posts", json=payload)
        assert response.status_code == 201
        assert response.json()["title"] == "foo"
        assert response.json()["body"] == "bar"
        assert response.json()["userId"] == 1
