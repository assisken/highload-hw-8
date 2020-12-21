from kafka import KafkaConsumer
from kafka.consumer.fetcher import ConsumerRecord

consumer = KafkaConsumer('dead_letter', bootstrap_servers=['localhost:9091'], api_version=(0, 10, 1))

for msg in consumer:
    msg: ConsumerRecord
    print(f'DEBUG: {msg}')
