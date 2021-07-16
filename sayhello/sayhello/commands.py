import click
from sayhello import app, db
from sayhello.models import Message

@app.cli.command() # app.cli.集成在flask中的装饰器，flask可以直接调用
@click.option('--drop', is_flag=True, help='Create after drop.') # option添加选项
def initdb(drop):
    '''在cli中直接使用

    flask initdb
    '''
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('initialied database.')

@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    '''generate fake messages'''
    from faker import Faker

    db.drop_all()
    db.create_all()

    # 实例化Faker类，传入locale参数zh_CN，能生成中文
    fake = Faker('zh_CN')
    click.echo('working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
            )
        db.session.add(message)

    db.session.commit()
    click.echo(f'create {count} fake messages.')