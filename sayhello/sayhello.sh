cd D:\ryanoligen\python_fullstack\flask
python -m venv env
.\env\Scripts\activate
pip install flask
pip install flask-dotenv
pip install flask-sqlalchemy
pip install flask-wtf
pip install bootstrap-flask
# 需要安装的包
# Bootstrap-Flask
# Flask-Moment
# Faker
# Flask-DebugToolbar

mkdir sayhello
cd .\sayhello
type nul>sayhello.sh # cmd 创建.sh脚本文件，PS下不行 ?qm

# 创建存储环境变量的文件，在哪个路径下?qm
type nul>.flaskenv 

# # 开发规范
# 需求说明书-->功能规格、技术规格书
# 草图-->原型图(aurxe mockplus)-->前端
# 数据库建模（建模工具）-->表单类-->视图函数

# 建模 models.py Message
# 自定义flask命令 commands.py flask initdb
# 表单类 forms.py HelloForm
# 视图views.py index (缺错误处理函数)
# 编写模板 templates base.html index.html