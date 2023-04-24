import argparse

from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from src.entity.generic import Generic
from src.kafka_config import sasl_conf
from src.database.mongodb import MongodbOperation




def consumer_using_sample_file(topic,file_path):

    schema_str = Generic.get_schema_to_produce_consume_data(file_path=file_path)
    #converting dict to object
    json_deserializer = JSONDeserializer(schema_str,
                                         from_dict=Generic.dict_to_object)
     #to connect with kafka server
    consumer_conf = sasl_conf()
    #it is a kind of a tracker in consumer,who has received what amount of data
    #based on the id it knows how much data this grp has received
    #it receive the data from kafka
    consumer_conf.update({
        'group.id': 'group1',
        'auto.offset.reset': "earliest"})
    
    #creating the consumer
    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])

    mongodb = MongodbOperation()
    #storing the 5000 records and then inserting them in db
    records = []
    x = 0
    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            #we will get object after deserialize the data from dict to object
            #1 object record will have all the sensors readings
            record: Generic = json_deserializer(msg.value(), SerializationContext(msg.topic(), MessageField.VALUE))

            # mongodb.insert(collection_name="car",record=car.record)

            if record is not None:
                records.append(record.to_dict())
                # keep appending the records in list and when x value becomes 5000 then only it will send the data
                if x % 5000 == 0:
                    mongodb.insert_many(collection_name="car", records=records)
                    records = []
            x = x + 1
        except KeyboardInterrupt:
            break

    consumer.close()
