import json, os, django
from confluent_kafka import Consumer
# import pika    #For RabbitMQ Conection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.apps import apps

Cart = apps.get_model('cart', 'Cart')


consumer = Consumer({
    'bootstrap.servers': 'pkc-6ojv2.us-west4.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'JZXOGUTCMHVIMSFM',
    'sasl.password' : 'F0CY4IGDc5RYz1RkiG4lnf5tz+pWwSwKF13UrH2oc3Z+7ulPtZkWAVqbh/KUn/PV',
    'sasl.mechanisms': 'PLAIN',
    'group.id': 'cart_consumer',
    'auto.offset.reset': 'earliest',    
})

consumer.subscribe(['user_registered'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    
    print('Received message with Value: {}'.format(msg.value().decode('utf-8')))
    print('Message Topic: {}'.format(msg.topic()))
    print ('Message Key: {}'.format(msg.key()))

    topic = msg.topic()
    value = msg.value().decode('utf-8')

    if topic == 'user_registered':
        if msg.key() == b'create_user':
            user_data = json.loads(value)
            user_id = user_data['user_id']

            cart, created = Cart.objects.get_or_create(user_id=user_id, defaults={'total_items': 0})
            if created:
                cart.save()
        pass

    
consumer.close()
        
# # Conexión a RabbitMQ
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='amqps://guodpncs:dK74rfmJrGCEAfsWNaqO0D-6bJWLMPSa@shrimp.rmq.cloudamqp.com/guodpncs'))
# channel = connection.channel()

# # Declaración de la cola
# channel.queue_declare(queue='auth_queue')

# def callback(ch, method, properties, body):
#     # Decodificación del mensaje
#     message = json.loads(body)

#     # Obtención del usuario
#     try:
#         user = User.objects.get(username=message['username'])
#     except User.DoesNotExist:
#         # Creación del usuario si no existe
#         user = User.objects.create_user(username=message['username'], password='password')

#     # Obtención del carrito del usuario
#     try:
#         cart = Cart.objects.get(user=user)
#     except Cart.DoesNotExist:
#         # Creación del carrito si no existe
#         cart = Cart.objects.create(user=user)

#     # Actualización del carrito
#     cart.total_price = message['total_price']
#     cart.save()

#     # Confirmación de recepción del mensaje
#     ch.basic_ack(delivery_tag=method.delivery_tag)

# # Consumo de mensajes
# channel.basic_consume(queue='auth_queue', on_message_callback=callback)

# print('Waiting for messages...')
# channel.start_consuming()