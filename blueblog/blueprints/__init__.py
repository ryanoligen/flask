import os, sys

from flask import Flask
from blueblog.settings import config
from blueblog.extensions import 

def register_logging(app):
    pass

# 为程序实例注册扩展类
def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

def register_blueprints(app):
    # 在程序实例上注册蓝本
    app.register_blueprint(blog)
    # 设置参数url_prefix，访问蓝本的url会添加prefix
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(auth, url_prefix='/auth')

# ?qm 为什么是db
# 注册上下文
def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)

# 注册模板上下文
def register_template_context(app):
    pass

# 注册400错误页面
def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

# 注册自定义flask命令
def register_commands(app):
    pass

# 工厂函数 返回程序实例（返回的是类）
# flask自动发现实例程序的机制，会在flask run运行时，若存在create_app或make_app，则自动调用
def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    # 实例化程序
    app = Flask('blueblog')
    # 根据不同的环境，导入不同的配置
    app.config.from_object(config[config_name])

    register_logging(app)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errors(app)
    register_shell_context(app)
    register_template_context(app)
    return app




