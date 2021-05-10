import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
p = r.pubsub()
while True:
    p.subscribe('chat')

    for info in p.listen():
        try:
            mess = json.loads(info.get('data'))
            print(f"{mess.get('name')}: {mess.get('message')}")
        except:
            continue
