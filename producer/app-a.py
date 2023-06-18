from pymongo import MongoClient
from kafka import KafkaProducer
import json
import time
import os 
# MongoDB bağlantı bilgilerini güncelleyin
mongo_host = "mongodb://mongo:27017/"
mongo_db = os.environ["MONGODB_DB"]
mongo_collection = os.environ["MONGODB_COLLECTION"]

# Kafka bağlantı bilgilerini güncelleyin
kafka_bootstrap_servers = os.environ["KAFKA_BROKERCONNECT"]
kafka_topic = os.environ["KAFKA_TOPIC"]

# MongoDB'ye bağlanın
mongo_client = MongoClient(mongo_host)
db = mongo_client[mongo_db]
collection = db[mongo_collection]

# Kafka producer'ını yapılandırın
producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers)


last_count = collection.count_documents({})

sendJustOne = True

while True:
    #  5 saniye bekle
    time.sleep(5)

    # şuan ki doküman sayısını al 
    current_count = collection.count_documents({})

    # doküman sayısını karşılaştır
    if current_count > last_count:
        # yeni dokümanlar varsa, dokümanları Kafka'ya gönder
        new_documents = collection.find().skip(last_count)
        for document in new_documents:
            if(sendJustOne):
                print("send document:", document)

                document["_id"] = str(document["_id"])
            
                json_message = json.dumps(document)
                
                producer.send(kafka_topic, value=json_message.encode("utf-8"))       

                producer.flush()
                sendJustOne = False
        
        sendJustOne = True
        last_count = current_count




