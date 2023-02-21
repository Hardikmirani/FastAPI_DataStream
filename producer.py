# importing the required libraries  
from time import sleep
from json import dumps
from kafka import KafkaProducer
import csv

# initializing the Kafka producer  
my_producer = KafkaProducer(  
    bootstrap_servers = ['localhost:9092'],  
    value_serializer = lambda x:dumps(x).encode('utf-8')  
    )  

with open('TCS_dummy_data.csv') as file_obj:

    reader_obj = csv.reader(file_obj)

    for row in reader_obj:
        my_producer.send('testnum', value = row[8])
        sleep(0.5)

