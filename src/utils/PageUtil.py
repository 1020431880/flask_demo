import json

"""
分页工具类
"""


class PageUtil(object):
    def __init__(self):
        self._page_num = 1
        self._page_size = 10
        self._total_page = 0
        self._total_size = 0
        self._results = None

    # 当前页数
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        self._page_num = page_num

    # 每页显示条数
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        self._page_size = page_size

    # 总页数
    @property
    def total_page(self):
        if (self._total_size > 0):
            if (self._total_size % self._page_size == 0):
                self._total_page = self._total_size // self._page_size
                return self._total_page
            else:
                self._total_page = self._total_size // self._page_size + 1
                return self._total_page
        else:
            return 0

    @total_page.setter
    def total_page(self, total_page):
        self._total_page = total_page

    # 总条数
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        self._total_size = total_size

    # 列表数据
    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, results):
        self._results = results

    # 包装的数据转json
    def to_json(self):
        return {
            "page_num": self.page_num,
            "page_size": self.page_size,
            "total_page": self.total_page,
            "total_size": self.total_size,
            "results": self.results
        }
