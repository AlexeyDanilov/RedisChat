import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
print("Write your name:")
name = input()
while True:
    print("Write your message:")
    message = input()
    r.hset('messages', 'name', name)
    r.hset('messages', 'message', message)
    info = json.dumps(r.hgetall('messages'))
    r.publish('chat', info)