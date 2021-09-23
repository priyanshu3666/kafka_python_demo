from kafka import KafkaProducer
import json 
from regex_1 import get_result
import time
import random

def json_serializers(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers = ['192.168.1.9:9092'],value_serializer = json_serializers)


if __name__ =='__main__':
    for i in range(random.randint(4,7)):
        print(get_result())
        producer.send("regex_result",get_result())
        time.sleep(2)