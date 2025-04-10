import redis

def connect_redis():
    # activate this line if you've separately redis on your local
    # client = redis.StrictRedis(host='localhost', port=6379, db=0)

    # active this line if you're using docker
    client = redis.StrictRedis(host='redis', db=0)
    return client

def store_redis(message_id, message_result):
    client = connect_redis()
    client.set(message_id, message_result)

def get_redis(message_id):
    client = connect_redis()
    # print(f"redis_key: {message_id}")
    return client.get(message_id)

