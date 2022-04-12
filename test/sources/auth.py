from actions import (os, load_dotenv)
from elasticsearch import Elasticsearch

load_dotenv()

es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
)


#
connection = ConnectHandler(**AccessControllers.AC6005, conn_timeout=60)

command = 'display access-user'
output = connection.send_command(command)

WorldItem.lista_users = limpar_output(
    output,
    WorldItem.regx_userid
)

WorldItem.lista_users = separar_campos(
    WorldItem.lista_users
)

connection.disconnect()

print(WorldItem.lista_users)
