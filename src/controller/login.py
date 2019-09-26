from flask import jsonify, request, Blueprint, url_for, redirect
from flask import session

# 登陆模块路由
login = Blueprint('login', __name__)


@login.route('/loginin', methods=['post'])
def login_in():
    print(request.args)
    return jsonify({
        'code': 200,
        'data': '登陆成功，登陆的信息是：' + request.args
    })


@login.route('/loginout/', methods=['post'])
def login_out():
    print(request.form)
    return 'login ok'
