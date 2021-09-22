import pika
import time
import json

from faker import Faker

from config import (
  RUN,
  SLEEP,
  RABBITMQ_HOST,
  RABBITMQ_PORT,
  RABBITMQ_USERNAME,
  RABBITMQ_PASSWORD,
  RABBITMQ_EXCHANGE,
  RABBITMQ_QUEUE,
  RABBITMQ_ROUTING_KEY
)

# RabbitMQ

credentials = pika.PlainCredentials(
  username=RABBITMQ_USERNAME,
  password=RABBITMQ_PASSWORD
)

params = pika.ConnectionParameters(
  host=RABBITMQ_HOST,
  port=RABBITMQ_PORT,
  credentials=credentials
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(
  queue=RABBITMQ_QUEUE,
  durable=True
)

fake = Faker()

print("Productor corriendo")

while RUN:
  message = {
    "nombre": fake.name(),
    "dirección": fake.address()
  }

  channel.basic_publish(
    exchange=RABBITMQ_EXCHANGE,
    routing_key=RABBITMQ_ROUTING_KEY,
    body=str(message)
  )

  print(" [.] Mensaje enviado: %r" % message)

  time.sleep(SLEEP)
  


