from flask import Flask, request, jsonify
import pika
from consumer import start_consuming
from uuid_extensions import uuid7str
import json
from redis_serve import get_redis


app = Flask(__name__)

def send_to_rabbitmq(message):
    # activate this line if you've separately rabbitMQ on your local
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
    #                                                                port=5673,
    #                                                                virtual_host='/',
    #                                                                credentials=pika.PlainCredentials('guest', 'guest')))

    # active this line if you're using docker
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='gemini_queue')
    channel.basic_publish(
        exchange='', routing_key='gemini_queue', body=message)
    connection.close()


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')

    get_uuid = uuid7str()

    data_dict = {
        "id": get_uuid,
        "text": text,
    }

    message_body = json.dumps(data_dict)
    send_to_rabbitmq(message_body)

    return jsonify({
        "message_id": get_uuid,
        "question": text,
        "status": "Message sent to queue",
    }), 200


@app.route('/result',methods=['GET'])
def get_result():
    data = request.args
    msg_id = data.get('message_id')

    message = get_redis(msg_id)


    if message is not None:
        return jsonify({
            "result": message.decode('utf-8'),
        }), 200
    else:
        return jsonify({"error": "No result available"}), 404


if __name__ == '__main__':
    # import threading
    #
    # consumer_thread = threading.Thread(target=start_consuming)
    # consumer_thread.daemon = True
    # consumer_thread.start()

    app.run(host='0.0.0.0', port=5000, debug=True)
