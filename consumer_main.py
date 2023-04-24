#providing the topic name and passing the data file to get the schema
from src.kafka_consumer.json_consumer import consumer_using_sample_file

from src.constant import SAMPLE_DIR
import os
if __name__=='__main__':



    topics = os.listdir(SAMPLE_DIR)
    #print topic name
    print(f'topics: [{topics}]')
    for topic in topics:
        sample_topic_data_dir = os.path.join(SAMPLE_DIR,topic)
        #data file path
        sample_file_path = os.path.join(sample_topic_data_dir,os.listdir(sample_topic_data_dir)[0])
        #passing the file to create the structure by using file
        consumer_using_sample_file(topic="kafka-sensor-topic",file_path = sample_file_path)