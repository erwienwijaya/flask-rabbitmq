from flask import Flask, request, jsonify
import pika

app = Flask(__name__)


def send_to_rabbitmq(message):
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
    #                                                                port=5673,
    #                                                                virtual_host='/',
    #                                                                credentials=pika.PlainCredentials('guest', 'guest')))
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
    send_to_rabbitmq(text)
    return jsonify({
        "question": text,
        "status": "Message sent to queue"
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
