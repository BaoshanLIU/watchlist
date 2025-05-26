#从flask包中导入Flask类， class Flask
from flask import Flask, render_template
from markupsafe import escape

#通过实例化class Flask，创建了程序对象app
app = Flask(__name__)


name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)





#注册一个请求处理函数，官方名为 view function.
#用装饰器app.route()绑定对应的URL。当用户在浏览器访问这个URL时，就会触发这个函数，获取返回值。
@app.route('/lesson1')
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