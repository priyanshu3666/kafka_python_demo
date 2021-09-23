from kafka import KafkaConsumer
import json

from kafka.metrics.stats import rate

if __name__ == '__main__':
    consumer = KafkaConsumer(
        "Bank_rates",
        bootstrap_servers ='192.168.1.9:9092',
        auto_offset_reset='earliest',
        group_id ='consumer_group_4')
    print("stating the consumer")
    for msg in consumer:
        fetched_list  = json.loads(msg.value)
        rates = fetched_list.values()
        if ['BOB_rates'] == fetched_list['PNB_rates'] or ['SBI_rates'] ==fetched_list['PNB_rates'] or ['SBI_rates'] ==fetched_list['BOB_rates']:
            if fetched_list['BOB_rates'] == fetched_list['PNB_rates']:
                if fetched_list['BOB_rates']>fetched_list['SBI_rates']:
                    print("BOB gives equal  policy. to PNB  its rate is {}".format(fetched_list['BOB_rates']))
                if fetched_list['SBI_rates'] ==fetched_list['BOB_rates']:
                    print("SBI gives equal  policy. to PNB and BOB   its rate are {}".format(fetched_list['PNB_rates']))
                    
            if fetched_list['SBI_rates'] ==fetched_list['PNB_rates']:
                if fetched_list['BOB_rates']<fetched_list['SBI_rates']:
                    print("SBI gives equal  policy. to PNB  its rate is {}".format(fetched_list['SBI_rates']))
        else:                
            if fetched_list['BOB_rates']>fetched_list['PNB_rates'] and fetched_list['BOB_rates']>fetched_list['SBI_rates']:
                    print("BOB gives best policy. its rate is {}".format(fetched_list['BOB_rates']))
            else:
                if fetched_list['SBI_rates']>fetched_list['PNB_rates']:
                        print("SBI gives best policy. its rate is {}".format(fetched_list['SBI_rates']))
                else :
                        print("PNB gives best policy. its rate is {}".format(fetched_list['PNB_rates']))
                
        