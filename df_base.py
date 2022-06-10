from elasticsearch import Elasticsearch
from etl import Lista
import pandas as pd
import eland as ed
import os

global df

df_access_users = pd.DataFrame(Lista.users,
                               columns=["UserID", "Username", "IPADDRESS", "MAC",
                                        "Status", "@timestamp-py"]
                               )

df_stations_all = pd.DataFrame(Lista.stations,
                               columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
                                        'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID',
                                        "@timestamp-py"]
                               )

df_statistics = pd.DataFrame(Lista.statistics,
                             columns=["MAC", "PCKT_SENT", "PCKT_RECEIVED", "BYTES_SENT",
                                      "BYTES_RECEIVED", "WID_RATE_SENT", "WID_RATE_RECEIVED",
                                      "TRIGGER_R_TOTAL", "TRIGGER_R_FAILED", "STA_POWER_SAVE"]
                             )

df = pd.merge(df_access_users, df_stations_all, how='outer', on=['MAC'])

df = df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
df = df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
df = df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})

df = pd.merge(df, df_statistics, how='outer', on=['MAC'])
df = df.fillna(0)


#%%
