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
   
   # If you already have the new version of Docker, use the code below
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
   # run on locally only (development mode)
   python consumer.py
   ```
5. **View the result**<br />
   Send a GET request to the '/result?message_id=change_with_message_id' endpoint, through terminal directly or using <b>Postman</b>:<br />
   ```
   curl -X GET http://127.0.0.1:5000/result\?message_id\=<change_with_message_id> -H "Content-Type: application/json"
   ```
6. **Monitoring Queue**<br />
   Open your browser and then run the url below 
   ```
   http://localhost:15673
   
   # user = guest
   # password = guest
   ```
7. **Monitoring Redis**<br />
   Open your terminal and then run the code below
   ```
   # open redis cli
   docker exec -it <container_id or container_name> redis-cli
   
   # open redis cli using docker compose
   docker-compose exec <name_of_service> redis-cli
   
   # If you already have the new version of Docker, use the code below
   docker compose exec <name_of_service> redis-cli 
   
   # flush all data on redis (delete all unnecessary data)
   docker exec -it <container_id or container_name> redis-cli flushall
   ```
