"""
环境配置文件
"""


class Env(object):
    DEBUG = True  #
    SECRET_KEY = 'flask_sqlalchemy'  # key
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 修改时候是否追踪依赖
    SQLALCHEMY_POOL_TIMEOUT = 30  # 数据库连接池超时时间，默认10
    SQLALCHEMY_POOL_SIZE = 10  # 数据库连接池大小，默认5


# 本地local环境
class Local(Env):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/test'


# dev环境
class Dev(Env):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/test'


# pre环境
class Pre(Env):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/test'


# pro环境
class Pro(Env):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/test'


# 导出配置
config = {
    'local': Local,
    'dev': Dev,
    'pre': Pre,
    'pro': Pro
}
