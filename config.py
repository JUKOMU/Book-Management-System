class BaseConfig:
    TESTING = False

    SECRET_KEY = 'hard to guess string'
    # 数据库设置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    HOSTNAME = "13.78.119.4"
    PORT = "3306"
    USERNAME = "root"
    PASSWORD = "&+s=rp)K*5,*1"
    DATABASE = "book_management_system"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://"+USERNAME+":"+PASSWORD+"@"+HOSTNAME+":"+PORT+"/"+DATABASE+"?charset=utf8mb4"

class DevelopmentConfig(BaseConfig):
    # 开启debug
    DEBUG = True
class ProductionConfig(BaseConfig):
    DEBUG = False

