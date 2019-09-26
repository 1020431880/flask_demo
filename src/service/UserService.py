from src.models.Base import db
from src.models.User import User
import json

print('UserService')


class UserService(object):

    # 获得用户列表
    def query_users(self, page):
        sql = "select * from tb_user limit :start, :end "
        result_data = list(db.session.execute(sql, {"start": (page.page_num - 1) * page.page_size, "end": page.page_size}))
        result_list = []
        for item in result_data:
            result_list.append({
                'id': item[0],
                'name': item[1]
            })
        return result_list

    # 获取总条数
    def get_count(self):
        sql = "select count(id) from tb_user"
        result_data = list(db.session.execute(sql))[0]
        return int(result_data[0])

    # 根据id获得用户信息
    def get_user_byid(self, id):
        sql = "select id,name from tb_user where id=:id"
        result_data = list(db.session.execute(sql, {"id": id}))
        result_obj = None
        if (result_data and len(result_data) > 0):
            result_obj = {
                'id': result_data[0][0],
                'name': result_data[0][1]
            }
        return result_obj

    # 新增用户
    def add_user(self, user):
        try:
            db.session.add(user)
            db.session.commit()
            db.session.flush()
            return {
                'id': user.id,
                'name': user.name
            }
        except Exception as e:
            print(e)

    # 更新用户
    def update_user(self, user):
        try:
            res = db.session.query(User).filter(User.id == user.id).update({"name": user.name})
            db.session.commit()
            db.session.close()
            return res
        except Exception as e:
            print('出错了')

    # 根据id删除用户
    def delete_user_byid(self, id):
        pass
