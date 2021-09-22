from kafka import KafkaProducer
import json 
from ipl_web_scrapper import ipl_data_dict


def json_serializers(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers = ['192.168.1.9:9092'],value_serializer = json_serializers)


if __name__ =='__main__':
        producer.send("IPL_team_details",ipl_data_dict)