import redis
from connections_enum import ConnectionType


class RedisServe:
    def __init__(self, connection_type=ConnectionType.DOCKER):
        self.client = None
        if connection_type == ConnectionType.DOCKER:
            self.client = redis.StrictRedis(host='redis', port=6379, db=0)
        else:
            self.client = redis.StrictRedis(host='localhost', port=6379, db=0)

        try:
            # checking connection to redis
            self.client.ping()
            print("Connected to Redis established...")

        except redis.ConnectionError:
            print("Failed to connect to Redis server!")
            raise

    # set redis
    def store_redis(self, message_id, message_result):
        self.client.set(message_id, message_result)
        print(f"stored message_id: {message_id}")

    # get redis
    def get_redis(self, message_id):
        result = self.client.get(message_id)

        if result is None:
           print(f"no such message_id= {message_id}")
           return None
        else:
           print(f"result with message_id= {message_id} founded")
           return result

    # delete result by message_id
    def delete_redis(self, message_id):
        result = self.client.delete(message_id)

        if result is None:
            print(f"no such message_id= {message_id}")
        else:
            print(f"result with message_id= {message_id} deleted")

