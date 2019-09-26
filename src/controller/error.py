from flask import Flask, render_template, Blueprint

# 错误模块路由
error = Blueprint('error', __name__)


# 404页面
@error.errorhandler(404)
def internal_error_404():
    return render_template('errors/404.html')


# 500页面
@error.errorhandler(500)
def internal_error_500():
    return render_template('errors/500.html')
