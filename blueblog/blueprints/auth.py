from flask import Blueprint

# 构造蓝本
auth_bp = Blueprint('auth', __name__)


# 通过蓝本实例注册路由，装饰视图函数
@auth_bp.route('/login')
def login():
    pass

@auth_bp.route('/logout')
def logout():
    pass

