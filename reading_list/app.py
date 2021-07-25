from functools import reduce
import os, sys
import click

from flask import Flask, cli, render_template

from flask import request, url_for, redirect, flash, escape
from flask.typing import ResponseReturnValue # escape 对动态url传入的参数转义，起安全作用

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 数据库相关的配置项，以后可以用配置文件来设置配置项
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 关闭对模型修改的监控

# 设置密钥值，用于对请求中的数据进行签名
app.config['SECRET_KEY'] = 'dev'


db = SQLAlchemy(app) # 扩展类的使用，1.导入扩展类，2.以程序实例为参数实例化扩展类


# # 页面中的变量，在设置数据库后，可以从数据库读取数据
# user = 'ryan oligen'
# books = [
#     {'title': '霍乱时期的爱情', 'author': '加西亚 马尔克斯'},
#     {'title': '塔库东来', 'author': '王南'},
#     {'title': '如何阅读一本书', 'author': '埃德勒'},
#     {'title': 'Flask Web开发实战', 'author': '李辉'}
# ]



# 创建数据库模型
class User(db.Model): # 用户表，表名user
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20)) # 用户名

class Book(db.Model): # 书表，表名book
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60)) # 书名
    author = db.Column(db.String(10)) # 作者


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    '''注册一个命令行函数，利用click模块，?qm

    实现初始化数据库
    使用，命令行flask initdb
    flask initdb --drop
    '''
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('initialized database.')



@app.cli.command()
def forge():
    '''用函数把数据插入数据库
    
    使用方法cli: flask forge'''
    db.create_all()

    name = "ryan oligen"
    books = [
        {'title': '霍乱时期的爱情', 'author': '加西亚 马尔克斯'},
        {'title': '塔库东来', 'author': '王南'},
        {'title': '如何阅读一本书', 'author': '埃德勒'},
        {'title': 'Flask Web开发实战', 'author': '李辉'}
    ]

    user = User(name = name)
    db.session.add(user)
    for book in books:
        book_i = Book(title=book['title'], author=book['author'])
        db.session.add(book_i)
    
    db.session.commit()
    click.echo('insert data done.')


# 注册一个上下文处理函数，被装饰函数的返回值(dict)，能够在模板中直接使用
@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)


# 带参数的装饰器
# 处理错误请求，返回404页面, m
@app.errorhandler(404)
# 异常对象作为参数
def page_not_found(e): 
    # user = User.query.first()
    # return render_template('404.html', user=user), 404 # 需要返回渲染模板以及状态码404
    # 一般视图函数也有一个状态码返回值，默认200，可以不显示写出
    return render_template('404.html'), 404 # user已经在上文中，可以不传入



# 首页
@app.route('/')
def hello():
    '''首页
    
    '''
    return f"Welcome to <strong> Ryan </strong>'s 2021 reading list!" # 如何给reading list 添加链接 ?qm



# 阅读列表页
@app.route('/reading', methods=['GET', 'POST'])
def reading():
    '''2021阅读列表
    
    修改计划，多年的阅读列表，默认为当年。
        1.动态url
        2.默认值
        3.动态模板
    '''
    # user = User.query.first() # 从数据库读取第一条记录
    # books = Book.query.all()
    # return render_template('reading.html', user=user, books=books)
    # 有上下文处理函数，模板会直接在上下文中找变量user
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')

        # 验证表单数据是否存在，且长度符合字段要求
        if not title or not author or len(title) > 60 or len(author) > 10:
            flash('invalid input')
            return redirect(url_for('reading'))

        book = Book(title=title, author=author)
        db.session.add(book)
        db.session.commit()
        flash('item created')
        return redirect(url_for('reading'))

    books = Book.query.all()
    return render_template('reading.html', books=books)



@app.route('/book/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    book = Book.query.get_or_404(book_id)

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        if not title or not author or len(title) > 60 or len(author) > 10:
            flash('invalid input')
            return redirect(url_for('edit', book_id=book_id))

        book.title = title
        book.author = author
        db.session.commit()
        flash('item updated.')
        return redirect(url_for('reading'))

    return render_template('edit.html', book=book)


@app.route('/book/delete/<int:book_id>', methods=['POST'])
def delete(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('item deleted')
    return redirect(url_for('reading'))



# # 动态url页面
# @app.route('/user/<name>', defaults={'name': 'ryanoligen'})  # ?qm 如何使用默认值
# def user_page(name):
#     return f"this is user {name}'s page"

# # 测试url_for函数
# @app.route('/test')
# def test_url_for():
#     print(url_for('hello')) # 会在console输出
#     print(url_for('user_page', name='ryan'))
#     print(url_for('test_url_for'))
#     print(url_for('test_url_for', num=2)) # 不是试图函数的参数会被处理成搜索关键字
#     return 'Test page'
