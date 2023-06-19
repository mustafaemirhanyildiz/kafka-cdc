from kafka import KafkaConsumer
import os 
# Update connection information for Kafka
kafka_bootstrap_servers = os.environ["KAFKA_BROKERCONNECT"]
kafka_topic =os.environ["KAFKA_TOPIC"]
kafka_group_id = "mygroup"+ os.environ["ID"]

# Connect to Kafka

consumer = KafkaConsumer( 
    kafka_topic,
    bootstrap_servers= kafka_bootstrap_servers,
    group_id= kafka_group_id,)



while True:
    # Get all messages from Kafka
    for message in consumer:
         # print the message
        print("Recieve message: {}".format(message.value.decode("utf-8")))


    
   
