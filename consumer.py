import os
import time
import json
import google.generativeai as genai
from dotenv import load_dotenv
from connections import broker, client


load_dotenv()

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
    data_dict = json.loads(body.decode())

    print(f"Received message: {data_dict.get('text')}")
    result = process_with_gemini(data_dict.get('text'))

    client.store_redis(
        data_dict.get('id'),
        result,
    )

    print(result)


def start_consuming():
    channel_consume = broker.create_channel()
    channel_consume.queue_declare(queue='gemini_queue')
    channel_consume.basic_consume(queue='gemini_queue',
                                       on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')

    try:
        channel_consume.start_consuming()

        while True:
            pass  # keeping connection Alive

    except KeyboardInterrupt:
        print('Stopping consumer...')
        broker.connection.close()


if __name__ == '__main__':
    time.sleep(10) # set delay every in 10 seconds
    start_consuming()