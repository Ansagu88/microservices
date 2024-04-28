from confluent_kafka import Producer
import os

producer = Producer({
    'bootstrap.servers': 'pkc-6ojv2.us-west4.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'JZXOGUTCMHVIMSFM',
    'sasl.password' : 'F0CY4IGDc5RYz1RkiG4lnf5tz+pWwSwKF13UrH2oc3Z+7ulPtZkWAVqbh/KUn/PV',
    'sasl.mechanisms': 'PLAIN',   
})

# Produce a message
producer.produce('user_registered', key='my_key', value='my_value')

# Wait for any outstanding messages to be delivered and delivery reports to be received
producer.flush()