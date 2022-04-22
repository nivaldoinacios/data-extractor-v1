#!/usr/bin/python3
from elasticsearch import Elasticsearch, helpers
from pkg_rsrcs import csv, os
from utils import *
import pandas as pd

connection = ConnectHandler(**AccessControllers.AC6005,
                            conn_timeout=60)
connection.enable()

command = 'display access-user'
output = connection.send_command(command,
                                 read_timeout=30)

WorldItem.lista_users = limpar_output(
    output,
    WorldItem.regx_userid
)

WorldItem.lista_users = separar_campos(
    WorldItem.lista_users
)

time.sleep(1)

command = 'display station all'
output = connection.send_command(command)

WorldItem.lista_stations = limpar_output(
    output,
    WorldItem.regx_mac
)

WorldItem.lista_stations = separar_campos(
    WorldItem.lista_stations
)

command = 'display station statistics sta-mac '

WorldItem.lista_mac = gerar_lista_mac(
    WorldItem.lista_stations
)

for mac in WorldItem.lista_mac:
    output = connection.send_command(command + mac)
    output = output.replace(output[0:78], mac, 1)
    output = output.replace(output[-80:], '', 1)
    output = output.replace('Packets sent to the station', '')
    output = output.replace('Packets received from the station', '')
    output = output.replace('Bytes sent to the station', '')
    output = output.replace('Bytes received from the station', '')
    output = output.replace('Wireless data rate sent to the station(kbps)', '')
    output = output.replace('Wireless data rate received from the station(kbps)', '')
    output = output.replace('Trigger roam total', '')
    output = output.replace('Trigger roam failed', '')
    output = output.replace('STA power save percent', '')
    output = output.replace(':', '')
    output = output.replace(' ', '')
    output = output.split('\n')

    WorldItem.lista_statistics.append(output)

connection.disconnect()

# %%
df_access_users = pd.DataFrame(WorldItem.lista_users, columns=["UserID", "Username", "IPADDRESS", "MAC",
                                                               "Status", "@timestamp-py"])

df_stations_all = pd.DataFrame(WorldItem.lista_stations,
                               columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
                                        'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID',
                                        "@timestamp-py"])

df_statistics = pd.DataFrame(WorldItem.lista_statistics,
                             columns=["MAC", "PCKT_SENT", "PCKT_RECEIVED", "BYTES_SENT",
                                      "BYTES_RECEIVED", "WID_RATE_SENT", "WID_RATE_RECEIVED",
                                      "TRIGGER_R_TOTAL", "TRIGGER_R_FAILED", "STA_POWER_SAVE"])

WorldItem.df = pd.merge(df_access_users, df_stations_all, how='outer', on=['MAC'])

WorldItem.df = WorldItem.df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
WorldItem.df = WorldItem.df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
WorldItem.df = WorldItem.df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})

WorldItem.df = pd.merge(WorldItem.df, df_statistics, how='outer', on=['MAC'])
WorldItem.df = WorldItem.df.fillna(0)

WorldItem.df.to_csv(path_or_buf=os.getenv('dados'), sep=';',
                    columns=['UserID', 'Username', 'IPADDRESS', 'MAC', 'Status', 'AP_ID',
                             'AP_NAME', 'RF/WLAN', 'BAND', 'Type', 'RX/TX', 'RSSI', 'VLAN',
                             'SSID', '@timestamp-py', "PCKT_SENT", "PCKT_RECEIVED", "BYTES_SENT",
                             "BYTES_RECEIVED", "WID_RATE_SENT", "WID_RATE_RECEIVED",
                             "TRIGGER_R_TOTAL", "TRIGGER_R_FAILED", "STA_POWER_SAVE"],
                    header=True, index=True, index_label='index', line_terminator='\n')

#%%
