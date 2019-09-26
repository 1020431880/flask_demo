import os

bind = '127.0.0.1:8000'  # 服务绑定访问的ip
workers = 1  # 开启的工作进程数，也可以用 multiprocessing.cpu_count()获取cpu个数
threads = 2  # 每个工作进程的线程数
daemon = 'false'  # 设置守护进程，将进程交给supervisor管理，在生产环境下可以打开，防止关闭服务器连接后程序挂掉
worker_class = 'gevent'  # 工作模式，默认sync，可以安装用gevent
worker_connections = 1000  # 最大客户端并发连接数，默认1000，只适用于eventlet，gevent工作模式
timeout = 30  # 超时时间，默认是30
backlog = 2048  # 最大挂起的连接数，默认是2048
debug = True  # 是否开启debug模式
loglevel = 'debug'  # 输入日志的级别
accesslog = 'logs/catalina.log'  # 日志文件路径
errorlog = 'logs/error.log'  # 错误日志文件路径
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%({X-Real-IP}i)s"'  # 日志记录的格式
