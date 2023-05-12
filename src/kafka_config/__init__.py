
import os

#it allows kafa(server) and IOT DEVICE(client) to make a secure connection, it allows client and server to communicate

#authentication related variables
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"


#cloud api details. cluster related info
API_KEY = "H3W2IQXGETQZBNUWER" 
API_SECRET_KEY =  "7vuJ1RQgIGOA9Hby2f13nhfd4Slih5uD/ubmbg6rKNt6jTgaDc6FqfGCNPpmIBsghd" 
BOOTSTRAP_SERVER = "pkc-xrnwx.asia-south2.gcp.confluent.cloud:909"

#schema related variables
ENDPOINT_SCHEMA_URL  = "https://psrc-znpo0.ap-southeast-2.aws.confluent.cloud"
SCHEMA_REGISTRY_API_KEY = "SZYXSWDFZEBRRFrtr" 
SCHEMA_REGISTRY_API_SECRET = "+LY68DPHY+bCRCtmVuLaPVgRoKCZmdWoakMoJ46mSO8a698TwC4MfpDIeXophkdjjem"


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

