import pytest
import requests

BASE_URL = "http://kdtx-test.itheima.net"

class TestCoreAPI:
    def test_login_and_add_course(self):
        # 获取uuid
        captcha_resp = requests.get(f"{BASE_URL}/api/captchaImage")
        # 断言
        assert captcha_resp.status_code == 200
        uuid = captcha_resp.json().get("uuid")
        assert uuid is not None
        code = "2"

        # 登录
        # 发送POST请求
        login_resp = requests.post(f"{BASE_URL}/api/login", json={
            "username": "admin",
            "password": "HM_2023_test",
            "code": code,
            "uuid": uuid
        })

        # 断言
        assert login_resp.status_code == 200
        assert login_resp.json().get("code") == 200

        # 拿到token
        token = login_resp.json().get("token")
        assert token is not None

        # 新增课程
        # 发送POST请求添加课程。
        headers = {"Authorization": f"Bearer {token}"}
        course_data = {
            "name": "添加课程张张张",
            "subject": "6",
            "price": 999,
            "applicablePerson": "2"
        }
        # 断言
        course_resp = requests.post(f"{BASE_URL}/api/clues/course", json=course_data, headers=headers)
        assert course_resp.status_code == 200
        assert course_resp.json().get("code") == 200
        print("课程创建成功，响应：", course_resp.json())