from flask_sqlalchemy import SQLAlchemy
# 生成db操作对象
db = SQLAlchemy()


# 使用flask_sqlalchemy查询到的实体类转化为json格式
def db_to_json(self):
    is_list = self.__class__ == [].__class__
    is_set = self.__class__ == set().__class__
    if is_list or is_set:
        obj_arr = []
        for o in self:
            dict = {}
            a = o.__dict__
            if "_sa_instance_state" in a:
                del a['_sa_instance_state']
            dict.update(a)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        a = self.__dict__
        if "_sa_instance_state" in a:
            del a['_sa_instance_state']
        dict.update(a)


# 绑定转换方法到db中
db.db_to_json = db_to_json
