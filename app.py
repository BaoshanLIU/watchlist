#从flask包中导入Flask类， class Flask
from flask import Flask
from markupsafe import escape

#通过实例化class Flask，创建了程序对象app
app = Flask(__name__)

#注册一个请求处理函数，官方名为 view function.
#用装饰器app.route()绑定对应的URL。当用户在浏览器访问这个URL时，就会触发这个函数，获取返回值。
@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'

@app.route('/index2')
def hello2():
    return '欢迎来到我的 Watchlist！'

@app.route('/index3')
def hello3():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/home')
@app.route('/index')
def hello4():
    return 'Welcome to My Watchlist!'




@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'