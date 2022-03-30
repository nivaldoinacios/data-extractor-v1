# import access_user
# import stations
#
from elasticsearch import Elasticsearch
import pandas as pd
import json
import os


es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
)

df_users = pd.read_csv(os.getenv('dir_users'), delim_whitespace=True)
df_users.columns = ["UserID", "Username", "IPADDRESS", "MAC",
                    "Status", "@timestamp-py"]

df_stations = pd.read_csv(os.getenv('dir_stations'), delim_whitespace=True)
df_stations.columns = ['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
                       'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID', "@timestamp-py"]

df_users_stations = pd.merge(df_users, df_stations, on=['MAC'])
df_users_stations = df_users_stations.drop(columns=['IPADDRESS_x','@timestamp-py_y'])

#metodo para imprimir o dataframe em .csv
df_users_stations.to_csv(os.getenv('dir_users_stations'), index=False)
####INDEX ELASTIC
##MÉTODO TEMPORARIO
#####@cria um arquivo json
# doc = df_users_stations.to_json('doc.json', orient='columns')
#####@cria uma variavel q recebe o dataframe convertido em json
# doc = df_users_stations.to_json(orient='columns')
# #####@Index, auto id,
# resp = es.index(index="test-index", document=doc)
# print(resp['result'])


#%%
