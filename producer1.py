from kafka import KafkaProducer
import json 
from data import get_registered_user
import time
import random

def json_serializers(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers = ['192.168.1.9:9092'],value_serializer = json_serializers)


if __name__ =='__main__':
    for i in range(random.randint(5,11)):
        register_user = get_registered_user()
        print(register_user)
        producer.send("user_registration",register_user)
        time.sleep(2)