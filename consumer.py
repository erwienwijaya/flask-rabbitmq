import pika
import time

# Assume 'Gemini' is a placeholder for the actual large language model
def process_with_gemini(text):
    # Placeholder function for processing text with the Gemini model
    # this is example result from LLM Gemini
    result = {
        'sentiment': 'positive',
        'confidence': 0.95
    }
    return f"Scoring result: {result}"

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")
    result = process_with_gemini(body.decode())
    print(result)

def start_consuming():
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
    #                                                                port=5672,
    #                                                                virtual_host='/',
    #                                                                credentials=pika.PlainCredentials('guest','guest')))
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='gemini_queue')
    channel.basic_consume(queue='gemini_queue', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    time.sleep(10)  
    start_consuming()
