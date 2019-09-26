from flask import Flask, render_template, session, request
# 引入本地配置文件
from src.resources.env import config
# 引入数据库db
from src.models.Base import db
# 引入路由文件
from src.controller.error import error
from src.controller.login import login
from src.controller.user import user

# flask生成app，重新定义静态资源和页面位置
app = Flask(__name__, template_folder="webapp/templates", static_folder="webapp/static")

# 获取配置文件信息，常用的是from_object和from_pyfile方式
app.config.from_object(config['local'])
app.config.from_pyfile('src/resources/config.py', silent=True)
app.config["APPLICATION_ROOT"] = "flask_demo"
# 获取配置用app.config['API_URL']，或者app.config('API_URL')。区别是参数不存在的时候get不会报错，会返回None
# print('加载所有的配置：', app.config['SQLALCHEMY_DATABASE_URI'], app.config.get('SQLALCHEMY_DATABASE_URI'))

# 注册数据库的DB
db.init_app(app)


# 路由拦截器
@app.before_request
def request_interceptors():
    print('拦截请求')
    print("请求地址：" + str(request.path))
    print("请求方法：" + str(request.method))
    print("---请求headers--start--")
    print(str(request.headers).rstrip())
    print("---请求headers--end----")
    print("GET参数：" + str(request.args))
    print("POST参数：" + str(request.form))


# 注册蓝图全局路由
app.register_blueprint(error, url_prefix='/error')
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(user, url_prefix='/user')


@app.route("/index")
def index():
    return render_template("index.html", userName="admin")


if __name__ == '__main__':
    app.run()
