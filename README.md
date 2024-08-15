# Flask Gemini RabbitMQ Microservice

## Introduction

This project is a simple example of integrating Flask, RabbitMQ, and large language models like Gemini into a Python microservice.

## How to run

1. **Clone Repositori:**
   Clone or download directly.
   ```
   git clone (https://github.com/erwienwijaya/flask-rabbitmq.git)
   cd flask_gemini_rabbitmq
   ```
2. **Run the application using Docker Compose**
   ```
   docker-compose up --build
   ```
3. **Send a request**
   Send a POST request to the '/analyze' endpoint, through terminal directly or using postman:
   ```
   curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"text": "This sentiment analysis is very positive"}'
   ```
4. **View the result**
   The rabbitMQ consumer will receive the message and process it using the Gemini model. the result will be printed in the terminal.
