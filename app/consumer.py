from kafka import KafkaConsumer, KafkaProducer
from kafka.consumer.fetcher import ConsumerRecord

from models import Message, MessageType

consumer = KafkaConsumer('main_topic', bootstrap_servers=['localhost:9091'], api_version=(0, 10, 1))
producer = KafkaProducer(bootstrap_servers=['localhost:9091'], api_version=(0, 10, 1))

for msg in consumer:
    msg: ConsumerRecord
    print(f'DEBUG: {msg}')
    message = Message.from_json(msg.value.decode('utf8'))
    if message.type == MessageType.message:
        print('Done!')
    elif message.type == MessageType.error:
        producer.send('dead_letter', msg.value)
    else:
        raise ValueError('Unexpected behaviour')
