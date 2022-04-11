from elasticsearch import Elasticsearch, helpers
import pandas as pd
import eland as ed
import numpy as np
from etl import df
import csv
import os


es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
)


df.to_csv(path_or_buf=os.getenv('dir_users_stations'), sep=';',
          columns=['UserID', 'Username', 'IPADDRESS', 'MAC', 'Status', 'AP_ID',
                   'AP_NAME', 'RF/WLAN', 'BAND', 'Type', 'RX/TX', 'RSSI', 'VLAN',
                   'SSID', '@timestamp-py'],
          header=True, index=True, index_label='index', line_terminator='\n')

with open(os.getenv('dir_users_stations'), 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    helpers.bulk(es, reader, index='teste1')
#%%
