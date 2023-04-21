#here we have topic and file location 
from src.kafka_producer.json_producer import product_data_using_file
from src.constant import SAMPLE_DIR
import os
if __name__ == '__main__':
    
    #it will list all the folder inside sample data dir, topic will have all the folders name present in sample data
    topics = os.listdir(SAMPLE_DIR)
    #print the only topic we have inside the sample data directory
    print(f'topics: [{topics}]')
    for topic in topics:
        #sample data dir>> topic name 
        sample_topic_data_dir = os.path.join(SAMPLE_DIR,topic)
        #sample data >> topic name >> csv file
        sample_file_path = os.path.join(sample_topic_data_dir,os.listdir(sample_topic_data_dir)[0])
        product_data_using_file(topic=topic,file_path=sample_file_path)
