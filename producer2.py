from kafka import KafkaProducer
import json 
from data import get_movielist
import time
import random

def json_serializers(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers = ['192.168.1.9:9092'],value_serializer = json_serializers)


if __name__ =='__main__':
    for i in range(random.randint(5,11)):
        movies_data = get_movielist()
        print(movies_data)
        producer.send("movies_url",movies_data)
        time.sleep(2)