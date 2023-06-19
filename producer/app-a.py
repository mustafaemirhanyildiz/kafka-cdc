from pymongo import MongoClient
from kafka import KafkaProducer
import json
import time
import os 
# Update connection information for MongoDB
mongo_host = "mongodb://mongo:27017/"
mongo_db = os.environ["MONGODB_DB"]
mongo_collection = os.environ["MONGODB_COLLECTION"]

# Update connection information for Kafka
kafka_bootstrap_servers = os.environ["KAFKA_BROKERCONNECT"]
kafka_topic = os.environ["KAFKA_TOPIC"]

# Connect to MongoDB
mongo_client = MongoClient(mongo_host)
db = mongo_client[mongo_db]
collection = db[mongo_collection]


producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers)


last_count = collection.count_documents({})

sendJustOne = True

while True:
    #  wait 5 seconds
    time.sleep(5)

    # get current count of documents
    current_count = collection.count_documents({})

    # compare current count with last count
    if current_count > last_count:
        # if new documents are inserted, send them to kafka
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




