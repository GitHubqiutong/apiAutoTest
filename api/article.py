# 文章相关的 API
import requests

# 自媒体
from app import BASE_URL, MP_HEADER, MIS_HEADER, APP_HEADER


class PublishArticle:
    # 定义接口路径
    def __init__(self):
        self.pb_article_url = BASE_URL + "/mp/v1_0/articles"

    # 发布文章接口方法
    def test_pb_article(self, title, content, channel_id):
        # 定义数据
        params = {"title": title, "content": content, "channel_id": channel_id, "cover": {"type": 0, "images": []}}
        # 执行测试请求
        return requests.post(url=self.pb_article_url, json=params, headers=MP_HEADER)


# 后台管理系统
class MisArticle:

    # 查询文章方法
    def __init__(self):
        self.pb_article_url = BASE_URL + "/mis/v1_0/articles"
        self.ex_article_url = BASE_URL + "/mis/v1_0/articles"

    # 查询文章方法
    def test_qy_article(self, title, channel):
        # 定义测试数据
        query_string = {"title": title, "channel": channel}
        # 执行测试请求
        return requests.get(url=self.pb_article_url, params=query_string, headers=MIS_HEADER)

    # 审核文章方法
    def test_ex_article(self, ar_id, status):
        # 定义测试数据
        params = {"article_ids": [ar_id], "status": status}
        # 执行测试请求
        return requests.put(url=self.ex_article_url, data=params, headers=MIS_HEADER)


class AppArticle:
    def __init__(self):
        self.qy_at_byc_url = BASE_URL + "/app/v1_1/articles"

    def test_qy_at_by_channel(self, cl_id, timestamp, with_top):
        params = {"channel_id":cl_id, "timestamp":timestamp, "with_top": with_top}
        return requests.get(url=self.qy_at_byc_url, params=params, headers=APP_HEADER)
