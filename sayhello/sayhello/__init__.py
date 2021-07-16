# 程序启动时，构造文件__init__.py会首先被执行

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 从Bootstrap-Flask提供的包flask_bootstrap中导入Bootsrap，用于渲染Bootstrap模板
from flask_bootstrap import Bootstrap 

# 后端处理时间，前端js能够将其转换为本地化时间展示
from flask_moment import Moment

# 实例化程序，传入包名称
app = Flask('sayhello')
# # 从__name__变量获取包名称
# app = Flask(__name__.split('.')[0])


# 从py文件导入配置项
app.config.from_pyfile('settings.py')
# 设置模板环境，用来删除jinja语句后的第一个空行
app.jinja_env.trim_blocks = True
# 设置模板环境，删除jinja语句所在行之前的空格和制表符
app.jinja_env.lstrip_blocks = True


# 实例化扩展类
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

# 导入视图、错误（?qm）、自定义命令
from sayhello import views, errors, commands
