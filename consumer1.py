from kafka import KafkaConsumer
import json


if __name__ == '__main__':
    consumer = KafkaConsumer(
        "user_registration",
        bootstrap_servers ='192.168.1.9:9092',
        auto_offset_reset='earliest',
        group_id ='consumer_group_1')
    print("stating the consumer")
    for msg in consumer:
        print("Registered user = {}".format(json.loads(msg.value))) 