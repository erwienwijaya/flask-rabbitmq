from connections_enum import ConnectionType
from rabbitmq_serve import RabbitMQServe
from redis_serve import RedisServe

'''
Change ConnectionType:
- DOCKER = play it with docker
- MANUAL = play it for development
'''

# connection for Redis
client = RedisServe(connection_type=ConnectionType.DOCKER)

# connection for RabbitMQ
broker = RabbitMQServe(connection_type=ConnectionType.DOCKER)