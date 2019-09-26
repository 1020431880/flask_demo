import redis

conn = redis.Redis(host="127.0.0.1",port=6379)
# conn.set('name','张三丰',ex=10)
print(conn.get('name'))