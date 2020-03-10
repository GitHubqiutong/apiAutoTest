from api.article import PublishArticle, MisArticle, AppArticle
from api.login import MpLogin, MisLogin, AppLogin


class FactoryApi:

    # 自媒体登录类
    mp_login = MpLogin()
    publish_article = PublishArticle()
    # 后台管理系统登录类
    mis_login = MisLogin()
    mis_article = MisArticle()
    app_login = AppLogin()
    app_article = AppArticle()
