import pika
from connections_enum import ConnectionType

class RabbitMQServe:
    def __init__(self, connection_type=ConnectionType.DOCKER):
        self.connection = None
        self.channel_consume = None
        self.channel_publish = None

        try:
            if connection_type == ConnectionType.DOCKER:
                self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
            else:
                self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                    host='localhost',
                    port=5673,
                    virtual_host='/',
                    credentials=pika.PlainCredentials('guest', 'guest')
                ))

            print("Connected to RabbitMQ server...")

        except Exception as e:
            print("Failed to connect to RabbitMQ server: {}".format(e))


    def create_channel(self):
        if self.connection is not None and self.connection.is_open:
            return self.connection.channel()
        else:
            raise Exception("Connection is not established. Cannot create channel.")
