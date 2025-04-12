from flask import Flask, request, jsonify
from uuid_extensions import uuid7str
import json
from connections import broker, client

app = Flask(__name__)

def send_to_rabbitmq(message):
    channel_publish = broker.create_channel()
    channel_publish.queue_declare(queue='gemini_queue')
    channel_publish.basic_publish(
        exchange='', routing_key='gemini_queue', body=message)


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

    message = client.get_redis(msg_id)

    if message is not None:
        return jsonify({
            "result": message.decode('utf-8'),
        }), 200
    else:
        return jsonify({"error": "No result available"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
