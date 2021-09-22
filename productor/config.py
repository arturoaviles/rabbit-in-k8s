import os

RUN = bool(os.getenv("RUN", "True"))
SLEEP = int(os.getenv("SLEEP", "3")) # seconds

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", "5672"))
RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME", "")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "")
RABBITMQ_EXCHANGE = os.getenv("RABBITMQ_EXCHANGE", "")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "")
RABBITMQ_ROUTING_KEY = os.getenv("RABBITMQ_ROUTING_KEY", "")
