# 导包
import logging.handlers


class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取 日志器对象
            cls.logger = logging.getLogger()
            # 设置总结别
            cls.logger.setLevel(logging.INFO)
            # 根据时间切割 处理器
            th = logging.handlers.TimedRotatingFileHandler(filename="../log/tpshop.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8")
            # 设置处理器级别
            th.setLevel(logging.INFO)
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            # 格式器添加到处理器中
            th.setFormatter(fm)
            # 将处理器中 添加 日志器
            cls.logger.addHandler(th)
        return cls.logger
