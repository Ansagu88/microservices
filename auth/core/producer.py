from confluent_kafka import Producer
import os

def produce_message(topic, key, value):
    """
    Produces a message to the specified Kafka topic.

    Args:
        topic (str): The name of the Kafka topic to produce the message to.
        key (str): The key of the message.
        value (str): The value of the message.
    """
    producer = Producer({
        'bootstrap.servers': 'pkc-6ojv2.us-west4.gcp.confluent.cloud:9092',
        'security.protocol': 'SASL_SSL',
        'sasl.username': 'JZXOGUTCMHVIMSFM',
        'sasl.password' : 'F0CY4IGDc5RYz1RkiG4lnf5tz+pWwSwKF13UrH2oc3Z+7ulPtZkWAVqbh/KUn/PV',
        'sasl.mechanisms': 'PLAIN',   
    })

    # Produce a message
    producer.produce(topic, key=key, value=value)

    # Wait for any outstanding messages to be delivered and delivery reports to be received
    producer.flush()
