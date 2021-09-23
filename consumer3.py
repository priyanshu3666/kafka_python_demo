from kafka import KafkaConsumer
import json


if __name__ == '__main__':
    consumer = KafkaConsumer(
        "IPL_team_details",
        bootstrap_servers ='192.168.1.9:9092',
        auto_offset_reset='earliest',
        group_id ='consumer_group_2')
    print("stating the consumer")
    for msg in consumer:
        print("IPL team data  = {}".format(json.loads(msg.value))) 