from time import sleep

from kafka import KafkaProducer
from kafka.producer.future import FutureRecordMetadata

from models import Message, MessageType


def wait_until_sent(message: FutureRecordMetadata, *, delay: int = 1):
    while True:
        if message.succeeded():
            return
        sleep(delay)


producer = KafkaProducer(bootstrap_servers=['localhost:9091'], api_version=(0, 10, 1))

message = Message(type=MessageType.message, content='Hello, Bob!')
wait_until_sent(producer.send('main_topic', message.to_json().encode('utf8')))

message = Message(type=MessageType.error, content='Some error')
wait_until_sent(producer.send('main_topic', message.to_json().encode('utf8')))
