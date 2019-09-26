import os
import json
from flask import jsonify, request, Blueprint, abort
from src.service.UserService import *
from src.utils.PageUtil import PageUtil
from src.utils.ResponseData import ResponseData
from src.models.User import User
import traceback

# 用户模块路由
user = Blueprint('user', __name__)

# 引入service
userService = UserService()
# 引入返回对象和分页对象
pageUtil = PageUtil()
responseData = ResponseData()


# 获得用户列表
@user.route('/getUser', methods=['get'])
def get_user():
    # 组装查询的分页数据
    pageUtil.results = userService.query_users(pageUtil)
    pageUtil.total_size = userService.get_count()
    # 组装返回数据
    responseData.data = pageUtil.to_json()
    return jsonify(responseData.to_json())


# 根据ID获得用户信息
@user.route('/getUserById/<id>', methods=['get'])
def get_user_byid(id):
    result_data = userService.get_user_byid(id)
    return jsonify({'code': 200, 'message': '操作成功', 'data': result_data})


# 新增用户
@user.route('/addUser', methods=['post'])
def add_user():
    print(request.headers.get('BusiType'))
    userData = json.loads(request.data)
    u = User(name=userData.get('name'))
    responseData.data = userService.add_user(u)
    return jsonify(responseData.to_json())


# 更新用户
@user.route('/updateUser', methods=['post'])
def update_user():
    try:
        userData = json.loads(request.data)
        print(userData)
    except Exception as e:
        responseData.code = 500
        responseData.data = repr(e)
        responseData.message = "操作失败"
        return jsonify(responseData.to_json())
    # 请求数据正常
    u = User(id=userData.get('id'), name=userData.get('name'))
    responseData.data = userService.update_user(u)
    if responseData.data > 0:
        responseData.code = 200
        responseData.data = u.id
        responseData.message = "操作成功"
    else:
        responseData.code = 500
        responseData.data = "服务器更新数据失败"
        responseData.message = "操作失败"
    return jsonify(responseData.to_json())


# 上传用户头像
@user.route('/uploadHead', methods=['post'])
def upload_head():
    print(request.files)
    file = request.files.get('file')
    rootpath = '/Users/andy/PycharmProjects/flaskDemo/'
    uploadpath = os.path.join(rootpath, 'upload/', file.filename)
    file.save(uploadpath)
    return jsonify({'message': '操作成功'})
