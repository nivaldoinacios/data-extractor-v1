from elasticsearch import Elasticsearch
import csv

import eland as ed
import pandas as pd


from es_authentication import es

# Carrega pacotes netmiko.
import netmiko
from netmiko import ConnectHandler

# Carrega funcoes de tempo; data e hora.
from datetime import datetime
import time

# Carrega, respectivamente, pacotes para expressoes regex e funcoes do sistema operacional.
import re
import os
# Carrega o pacote que permite usarmos '.env' em python.
from dotenv import load_dotenv

#%%

load_dotenv()


#%%

# # Modelo de query/DataFrame com pandas a partir do index
res = es.search(index="heatmap*", size=100)
df = pd.json_normalize(res['hits']['hits'])
df
#df = pd.read_csv('', delim_whitespace=True)

#%%

df[['_source.Username','_source.RSSI']]

#%%
