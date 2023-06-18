from kafka import KafkaConsumer
import os 
# Kafka bağlantı bilgilerini güncelleyin
kafka_bootstrap_servers = os.environ["KAFKA_BROKERCONNECT"]
kafka_topic =os.environ["KAFKA_TOPIC"]
kafka_group_id = "mygroup"+ os.environ["ID"]

# Kafka consumer'ını yapılandırın

consumer = KafkaConsumer( 
    kafka_topic,
    bootstrap_servers= kafka_bootstrap_servers,
    group_id= kafka_group_id,)



while True:
    # Kafka'dan mesajları al
    for message in consumer:
         # Mesajı konsola yazdır
        print("Alınan Mesaj: {}".format(message.value.decode("utf-8")))


    
   
