from flask import flash, redirect, url_for, render_template



from sayhello import app, db
from sayhello.models import Message
from sayhello.forms import HelloForm

@app.route('/', methods=['GET', 'POST'])
def index():
    # 加载所有数据，按timestamp降序获取所有message
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    # 实例化表单类
    form = HelloForm()
    if form.validate_on_submit():
        # 如果是post请求，验证表单提交的内容
        # 获取提交的表单对应的数据
        name = form.name.data
        body = form.body.data
        # 实例化模型类，创建新的一条记录
        message = Message(body=body, name=name)
        # 添加记录到数据库会话
        db.session.add(message)
        # 提交会话
        db.session.commit()
        flash('your message have been sent to the world')
        # 重定向到index页面
        return redirect(url_for('index'))
    # 渲染index页面
    return render_template('index.html', form=form, messages=messages)



