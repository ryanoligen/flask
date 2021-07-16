from datetime import datetime
from sayhello import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 评论内容不超过200个字符
    body = db.Column(db.String(200))
    # 评论人名字不超过20个字符
    name = db.Column(db.String(20))
    # # 评论时间，timestamp字段设为索引
    # # !am attention mark. 这里用的是datetime.now 不是datetime.now()直接调用。与SQLAlchemy有关，慢慢理解
    # timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow) # datetime.utcnow不包含时区信息

