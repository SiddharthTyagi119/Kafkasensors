
import os

#it allows kafa(server) and IOT DEVICE(client) to make a secure connection, it allows client and server to communicate

#authentication related variables
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"


#cloud api details
API_KEY = "5ODTVLPKXBR4QA6F" 
API_SECRET_KEY =  "PxbejWolYltuhIyrjXXXldW+caDRVw16k6Dn64oFsLTE5wGmRMB/RhykXWz0WqVJ" 
BOOTSTRAP_SERVER = "pkc-41p56.asia-south1.gcp.confluent.cloud:9092"

#schema related variables
ENDPOINT_SCHEMA_URL  = "https://psrc-znpo0.ap-southeast-2.aws.confluent.cloud"
SCHEMA_REGISTRY_API_KEY = "326H6IPVGDGD7N5C" 
SCHEMA_REGISTRY_API_SECRET = "fF/ay0lEgQz8b1CjWcT06fRxHunS1V7krNJB7UaFgoxG4m2IMQ3CqbLWq6w6C6hq"


#this function will give us the kafka cluster configuration details
def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    #print(sasl_conf)
    return sasl_conf


#this function will give us the schema configuration details
def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

