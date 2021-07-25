# flask_project

## ch1
- . env/bin/activate
- deactivate

?qm

## ch2 
- 如果程序保存成非app.py，需要设置环境变量。环境变量如何设置，如何起作用
- 设置环境变量FLASK_ENV=development后，程序修改，刷新页面就能显示

- 设置多个路由地址，用url_for函数返回的url地址会是哪一个？ 
    - 经测试，是最底层的装饰器所指向的url地址