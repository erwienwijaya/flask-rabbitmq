# Flask Gemini RabbitMQ Microservice

## Introduction

This project is a simple example of integrating Flask, RabbitMQ, and Large Language Models (LLM) like Gemini into a Python microservice.

## Requirements:
- Python 3.12
- Flask
- RabbitMQ
- Redis
- Docker
- Gemini API Key (ensure you've already registered Gemini API)

## How to run

1. **Clone Repositori:**<br />
   Clone or download directly.<br/>
   ```
   git clone https://github.com/erwienwijaya/flask-rabbitmq.git
   cd flask-rabbitmq
   ```
2. **Run the application using Docker Compose**<br/>
   ```
   echo "GEMINI_API_KEY=your_key_api_here" >> .env
   docker-compose up --build
   
   # if you've already new version of docker use below it
   docker compose up --build
   ```
3. **Send a request**<br />
   Send a POST request to the '/analyze' endpoint, through terminal directly or using <b>Postman</b>:<br />
   ```
   curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d '{"text": "fun fact of Ruby"}'
   ```
4. **Activate the consumer (Don't need to run when using Docker compose)**<br />
   The rabbitMQ consumer will receive the message and process it using the Gemini model.<br />
   ```
   python consumer.py
   ```
5. **View the result**<br />
   Send a GET request to the '/result?message_id=change_with_message_id' endpoint, through terminal directly or using <b>Postman</b>:<br />
   ```
   curl -X GET http://127.0.0.1:5000/result\?message_id\=<change_with_message_id> -H "Content-Type: application/json"
   ```
6. **Monitoring Queue**<br />
   ```
   http://localhost:15673
   
   # user = guest
   # password = guest
   ```
