import access_user
import stations

from elasticsearch import Elasticsearch
from datetime import datetime
import pandas as pd
import json
import os
import re

es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
)

df_users = pd.read_csv(os.getenv('dir_users'), delim_whitespace=True)
df_users.columns = ["UserID", "Username", "IPADDRESS", "MAC",
                    "Status", "DATA", "HORA"]

df_stations = pd.read_csv(os.getenv('dir_stations'), delim_whitespace=True)
df_stations.columns = ['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
                       'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID', 'DATA', 'HORA']

df_users_stations = pd.merge(df_users, df_stations, on=['MAC'])
df_users_stations = df_users_stations.drop(columns=['DATA_x', 'HORA_x'])

#metodo para imprimir o dataframe em .csv
# df_users_stations.to_csv(os.getenv('dir_users_stations'), index=False)
#%%
####INDEX ELASTIC
##MÉTODO TEMPORARIO
doc = df_users_stations.to_json(orient='columns')
print(doc)
id_doc = 1
id_doc = id_doc + 1
resp = es.index(index='heatmap*', id=id_doc, document=doc)
print(resp['result'])

#%%
