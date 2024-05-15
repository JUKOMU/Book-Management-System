class BaseConfig:
    TESTING = False

    SECRET_KEY = 'hard to guess string'
    # 数据库设置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 设置是否追踪数据库变化  一般不会开启, 影响性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 设置是否打印底层执行的SQL语句
    SQLALCHEMY_ECHO = False
    HOSTNAME = "127.0.0.1"
    # 主库
    PORT_MASTER = "3306"
    # 从库
    PORT_SLAVE = "3307"
    USERNAME = "root"
    PASSWORD = "123"
    DATABASE = "book_management_system"
    # 设置数据库的连接地址
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + USERNAME + ":" + PASSWORD + "@" + HOSTNAME + ":" + PORT_MASTER + "/" + DATABASE + "?charset=utf8mb4"
    # 设置数据库的绑定地址
    SQLALCHEMY_BINDS = {"master": SQLALCHEMY_DATABASE_URI,
                        "slave": "mysql+pymysql://" + USERNAME + ":" + PASSWORD + "@" + HOSTNAME + ":" + PORT_SLAVE + "/" + DATABASE + "?charset=utf8mb4"
                        }


class DevelopmentConfig(BaseConfig):
    # 开启debug
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False