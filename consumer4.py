from kafka import KafkaConsumer
import json


if __name__ == '__main__':
    consumer = KafkaConsumer(
        "Bank_rates",
        bootstrap_servers ='192.168.1.9:9092',
        auto_offset_reset='earliest',
        group_id ='consumer_group_4')
    print("stating the consumer")
    for msg in consumer:
        print("Bank rates  = {}".format(json.loads(msg.value))) 