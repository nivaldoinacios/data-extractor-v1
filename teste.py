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

timestamp = datetime.now()
timestamp = timestamp.strftime('%d/%m/%Y %H:%M')


switch_1 = {
    'device_type': 'huawei',
    'host': '172.17.1.150',
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 0.1,
}

start = time.time()

connection = ConnectHandler(**switch_1)
connection.enable()
command = 'display access-user'

outputA = connection.send_command(command)
outputB = str(outputA)
output = outputA

connection.disconnect()

print(output)

# Escreve o valor de output em um arquivo csv se atender a busca condicional.

with open(os.getenv('PATH_DIS_ACC_USERS'), 'a') as arquivo:
    output = output.split('\n')

    for valor in output:
        if re.search('^\s([\d]{1,4})', str(valor)) is None:
            pass
        else:
            arquivo.write(str(valor) + ' ' + timestamp + '\n')

#%%

# # Modelo de query/DataFrame com pandas a partir do index
# res = es.search(index="heatmap*", size=100)
# df = pd.json_normalize(res['hits']['hits'])
# df

df = pd.read_csv('', delim_whitespace=True)

#%%
