#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Confluent Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# A simple example demonstrating use of JSONSerializer.

import argparse
from uuid import uuid4
from src.kafka_config import sasl_conf, schema_config
from six.moves import input
from src.kafka_logger import logging
from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
import pandas as pd
from typing import List
from src.entity.generic import Generic, instance_to_dict

FILE_PATH = "/home/avnish/iNeuron_Private_Intelligence_Limited/industry_ready_project/projects/data_pipeline/kafka-sensor/sample_data/sensor/aps_failure_training_set1.csv"


def car_to_dict(car: Generic, ctx):
    """
    Returns a dict representation of a User instance for serialization.
    Args:
        user (User): User instance.
        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.
    Returns:
        dict: Dict populated with user attributes to be serialized.
        :param car:
    """

    # User._address must not be serialized; omit from dict
    return car.record

#it is a kind of an acknowledgement that will raise the error if there is any issue
def delivery_report(err, msg):
    """
    Reports the success or failure of a message delivery.
    Args:
        err (KafkaError): The error that occurred on None on success.
        msg (Message): The message that was produced or failed.
    """

    if err is not None:
        logging.info("Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    logging.info('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))

#getting the schema by passing the file location
#function to generate the schema
def product_data_using_file(topic,file_path):
    logging.info(f"Topic: {topic} file_path:{file_path}")
    schema_str = Generic.get_schema_to_produce_consume_data(file_path=file_path)
    #getting the secrets and keys from kafka portal
    schema_registry_conf = schema_config()
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)

    #we have created a function to convert the object into the format of dict so that it can be utilize by json seralizer
    #seralize the object. seralizing the data. converting the data in a certain format so that it can be stored in a disk
    string_serializer = StringSerializer('utf_8')
    #seralizing the data object into dict
    #calling the object to dict and it will give you the object in form of dict
    #then you can serialize the object
    json_serializer = JSONSerializer(schema_str, schema_registry_client, instance_to_dict)



########## Producer ###########################
#to produce the data to kafka
    #creating producer class, just to connect with kafka server
    producer = Producer(sasl_conf())

    print("Producing user records to topic {}. ^C to exit.".format(topic))
    # while True:
    # Serve on_delivery callbacks from previous calls to produce()
    #it will make sure data is produce successfully when we send any data 
    producer.poll(0.0)
    try:
        #reading specific no. of records at a time and preparing the object then send that object to kafka
        #it will pick the one row from csv and create the object and in return it will give you the dict object
        #read data >>create object >>send data to kafka
        for instance in Generic.get_object(file_path=file_path):
            print(instance)
            logging.info(f"Topic: {topic} file_path:{instance.to_dict()}")
            producer.produce(topic=topic,
                             key=string_serializer(str(uuid4()), instance.to_dict()),
                             value=json_serializer(instance, SerializationContext(topic, MessageField.VALUE)),
                             on_delivery=delivery_report) #delivery report- acknowledging the data
            print("\nFlushing records...")
            producer.flush()
    except KeyboardInterrupt:
        pass
    except ValueError:
        print("Invalid input, discarding record...")
        pass

    
