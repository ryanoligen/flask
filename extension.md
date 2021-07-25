### 创建虚拟环境
python venv -m env  创建名为env的虚拟环境
虚拟环境激活、退出
. env/bin/activate
deactivate

## flask扩展
- flask-wtf # 表单
    - from flask_wtf import FlaskFrom
    - from wtforms import StringField, PasswordField, SubmitField
    - from wtforms.validators import DataRequired

- flask-sqlalchemy
    - from flask_sqlalchemy import SQLAlchemy

- flask-mail
    - from flask_mail import Mail

- bootstrap-flask
    - from flask_bootstrap import Bootstrap

- flask-moment
    - from flask_moment import Moment

- faker
    - from faker import Faker

- flask-debugtoolbar
    - from flask_debugtoolbar import DebugToolbarExtension
    