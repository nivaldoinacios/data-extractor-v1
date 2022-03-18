#Carrega os pacotes necessarios
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os
load_dotenv()

####
####
####
# class Users:
#     #função que define as propriedades que a classe terá
#     #__init__ cria a funcionalidade inicial da classe. Nesse caso cria as caracteriscas da classe.
#     def __init__(self, user_id=None, username=None, ipaddress=None, mac=None, status=None):
#         self.user_id = user_id
#         self.username = username
#         self.ipaddress = ipaddress
#         self.mac = mac
#         self.status = status
####
####
#ajustar HOST,USER E PASSWORD para seu ambiente.
es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
)
#####
#####
#%%
