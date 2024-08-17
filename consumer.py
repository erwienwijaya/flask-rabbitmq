import os
import pika
import time
import google.generativeai as genai


def process_with_gemini(askme):
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 80,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[
        ]
    )

    response = chat_session.send_message(askme)
    return response.text

    # this is example output, when hybrid with traditional machine learning had implemented
    # # result = {
    #     'sentiment': 'positive',
    #     'confidence': 0.95
    # }
    # return f"Scoring result: {result}"


def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")
    result = process_with_gemini(body.decode())
    print(result)


def start_consuming():
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
    #                                                                port=5673,
    #                                                                virtual_host='/',
    #                                                                credentials=pika.PlainCredentials('guest', 'guest')))
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='gemini_queue')
    channel.basic_consume(queue='gemini_queue',
                          on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    time.sleep(10)
    start_consuming()
