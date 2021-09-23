from kafka import KafkaConsumer
import json


if __name__ == '__main__':
    consumer = KafkaConsumer(
        "regex_result",
        bootstrap_servers ='192.168.1.9:9092',
        auto_offset_reset='earliest',
        group_id ='consumer_group_3')
    print("stating the consumer")
    for msg in consumer:
        print("Regex_result = {}".format(json.loads(msg.value))) 