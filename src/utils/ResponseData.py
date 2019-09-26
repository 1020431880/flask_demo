import json

"""
返回数据对象工具类
"""


class ResponseData(object):

    def __init__(self):
        self._code = 200
        self._message = "操作成功"
        self._data = None

    # code
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = int(code)

    # _message
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    # code
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    # 包装的数据转json
    def to_json(self):
        return {
            "code": self.code,
            "message": self.message,
            "data": self.data
        }
