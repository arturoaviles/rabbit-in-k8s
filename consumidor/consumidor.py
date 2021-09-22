import ast
import pika
import sys
import time
import os

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

def main():
    while RUN:
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

        print("Consumidor corriendo")

        def callback(ch, method, properties, body):
            print(" [x] Mensaje recibido: %r" % ast.literal_eval(body.decode()))
            time.sleep(SLEEP)


        channel.basic_consume(
            queue=RABBITMQ_QUEUE,
            on_message_callback=callback,
            auto_ack=True
        )

        print(' [*] Esperando mensajes. Para salir presione CTRL+C')
        channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)