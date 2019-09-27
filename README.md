
**1.导出到requirements.txt依赖的包： pip freeze >package.txt**
**2.在新的开发环境引入的时候安装依赖包：pip install -r  package.txt**
**3.运行gunicorn服务器：gunicorn -c gunicorn.py app:app**
