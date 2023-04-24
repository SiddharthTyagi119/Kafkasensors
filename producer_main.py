#here we have topic and file location 
from src.kafka_producer.json_producer import product_data_using_file
from src.constant import SAMPLE_DIR
import os
if __name__ == '__main__':
    
    #sample_dir = sample_data
    #it will list all the folder/dir inside sample data dir
    topics = os.listdir(SAMPLE_DIR)
    #print the only topic we have inside the sample data directory
    print(f'topics: [{topics}]')
    for topic in topics:
        #topic=kafka sensor topic
        #here we are just joining the sample dir and topic
        sample_topic_data_dir = os.path.join(SAMPLE_DIR,topic)
        #sample data >> topic name >> csv file
        #this is the path of data file 
        sample_file_path = os.path.join(sample_topic_data_dir,os.listdir(sample_topic_data_dir)[0])
        product_data_using_file(topic=topic,file_path=sample_file_path)
