# 文章发布-审核-查看流程
import pytest
from api import FactoryApi
from app import MP_HEADER, MIS_HEADER, APP_HEADER
import time
from utils.build_data import build_data


class TestPbArticle:
    article_id = None
    title = None

    # 前台登录
    def test_mp_login(self):
        # 定义数据
        mobile = "15811859004"
        code = "246810"
        # 调用登录方法
        mp_login_response = FactoryApi.mp_login.test_mp_login(mobile, code)
        print("自媒体登录结果返回信息为：{}".format(mp_login_response.json()))
        # 进行断言
        assert mp_login_response.status_code == 201
        assert mp_login_response.json().get("message") == "OK"
        # 获取登录后的token并存储
        mp_token = mp_login_response.json().get("data").get("token")
        print("自媒体登录后返回token信息为：{}".format(mp_token))
        # 添加token值到请求头
        MP_HEADER["Authorization"] = "Bearer " + mp_token
        print("提取mp_token值到请求头：{}".format(MP_HEADER))

    # 前台发布文章
    @pytest.mark.parametrize("ar_title, ar_content, ch_id,status_code,msg", build_data("data/data.json"))
    def test_article(self, ar_title, ar_content, ch_id, status_code, msg):
        # 定义测试数据
        self.title = ar_title.format(time.strftime("%Y%m%d:%H:%M:%S"))
        content = ar_content.format(time.strftime("%Y%m%d:%H:%M:%S"))
        channel_id = ch_id
        # 调用测试方法获取测试结果
        pb_al_response = FactoryApi.publish_article.test_pb_article(title=self.title, content=content, channel_id=channel_id)
        print("发布文章的响应结果为：{}".format(pb_al_response.json()))
        # 进行断言
        assert pb_al_response.status_code == status_code
        assert pb_al_response.json().get("message") == msg
        # 获取关联数据（*）
        TestPbArticle.article_id = pb_al_response.json().get("data").get("id")
        print("发布文章的id为：{}".format(TestPbArticle.article_id))
        # print("---------------------------------")
        return self.article_id

    # 后台登录
    def test_mis_login(self):
        # 定义测试数据
        username = "testid"
        password = "testpwd123"
        # 调用测试方法获取测试结果
        mis_login_response = FactoryApi.mis_login.test_mis_login(username, password)
        print("后台登录响应结果为：{}".format(mis_login_response.json()))
        # 执行测试断言
        assert mis_login_response.status_code == 201
        assert mis_login_response.json().get("message") == "OK"
        # 获取关联数据
        mis_token = mis_login_response.json().get("data").get("token")
        MIS_HEADER["Authorization"] = "Bearer " + mis_token
        print("添加mis_token值到请求头：{}".format(MIS_HEADER))

    # 后台查询文章
    def test_mis_article(self):
        # 定义测试数据
        article_title = self.title
        channel = "html"
        # 调用接口方法
        qy_response = FactoryApi.mis_article.test_qy_article(title=article_title, channel=channel)
        print("查询文章响应结果为：{}".format(qy_response.json()))
        # 执行测试断言
        assert qy_response.status_code == 200
        assert qy_response.json().get("message") == "OK"
        # print(qy_response.json().get("data").get("articles")[0].get("article_id"))
        assert qy_response.json().get("data").get("articles")[0].get("article_id") == TestPbArticle.article_id
        print(self.article_id)
        # 获取关联数据

    # 后台审核文章
    def test_ex_article(self):
        ar_id = TestPbArticle.article_id
        ar_status = 2
        ex_response = FactoryApi.mis_article.test_ex_article(ar_id, ar_status)
        print("发布文章响应为：{}".format(ex_response.json()))

    # App登录
    def test_app_login(self):
        # 定义测试数据
        mobile = "15811859004"
        code = "246810"
        ap_response = FactoryApi.app_login.test_app_login(mobile, code)
        print("app登录响应为：{}".format(ap_response.json()))
        app_token = ap_response.json().get("data").get("token")
        APP_HEADER["Authorization"] = "Bearer " + app_token
        print("提取app_token值到请求头：{}".format(APP_HEADER))

    # App查询文章
    def test_qy_al_by_cl(self):
        cl_id = 1
        timestamp = time.time() * 1000
        with_top = 1
        response = FactoryApi.app_article.test_qy_at_by_channel(cl_id, timestamp, with_top)
        print("app个根据频道查询文章响应为：{}".format(response.json()))
