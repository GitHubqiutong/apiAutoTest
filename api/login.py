import requests
from app import BASE_URL, MP_HEADER, MIS_HEADER, APP_HEADER


# 自媒体
class MpLogin:
    # 接口路径
    def __init__(self):
        self.mp_login_url = BASE_URL + "/mp/v1_0/authorizations"

    # 登录的测试方法
    def test_mp_login(self, mobile, code):
        """
        :param mobile:前台手机号
        :param code: 前台验证码
        :return:
        """
        # 定义数据
        params = {"mobile": mobile, "code": code}
        # 执行请求
        return requests.post(url=self.mp_login_url, json=params, headers=MP_HEADER)


# 后台管理系统
class MisLogin:
    # 接口路径
    def __init__(self):
        self.mis_login_url = BASE_URL + "/mis/v1_0/authorizations"

    # 测试方法
    def test_mis_login(self, username, password):
        """
        :param username:后台账号
        :param password: 后台密码
        :return:
        """
        # 测试数据
        params = {"account": username, "password": password}
        # 执行请求
        return requests.post(url=self.mis_login_url, json=params, headers=MIS_HEADER)


# App
class AppLogin:
    def __init__(self):
        self.app_login_url = BASE_URL + "/app/v1_0/authorizations"

    def test_app_login(self, mobile, code):
        params = {"mobile": mobile, "code": code}

        return requests.post(url=self.app_login_url, json=params, headers=APP_HEADER)
