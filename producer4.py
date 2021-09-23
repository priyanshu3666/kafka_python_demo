from random import randint
from kafka import KafkaProducer
import json 
from Bank_rates import Bank
import time
def json_serializers(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers = ['192.168.1.9:9092'],value_serializer = json_serializers)


if __name__ =='__main__':
    
    for i in range(randint(3,8)):
        bank_obj_consumer = Bank()
        bank_rates_dict ={
            'BOB_rates' :bank_obj_consumer.get_BOB(),
        'PNB_rates'  :bank_obj_consumer.get_PNB(),
        'SBI_rates'  : bank_obj_consumer.get_SBI()            
        }
        print(bank_rates_dict)
        
        producer.send("Bank_rates",bank_rates_dict)
        time.sleep(7)