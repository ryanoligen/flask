import os

# 从构造文件导入变量时，不需要注明构造文件所在路径，只需要从包名称导入，所以用from sayhello
from sayhello import app

# 数据库uri
dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')

# 获取环境变量SRCRET_KEY的值，没有则返回secret string
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string') 
# 关闭警告信息
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 获取数据库uri
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)


BOOTSTRAP_SERVE_LOCAL = True # 从本地加载静态资源 ?qm 是在settings中还是.flaskenv，还是app.config中
