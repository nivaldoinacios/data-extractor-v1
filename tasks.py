from dotenv import load_dotenv
from utils import *
import pandas as pd
import os

load_dotenv()

# unifica as listas dos dados obtidos e transforma-os: lista -> dataframe -> csv
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

WorldItem.df = pd.merge(df_access_users, df_stations_all, how='outer', on=['MAC'])

WorldItem.df = WorldItem.df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
WorldItem.df = WorldItem.df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
WorldItem.df = WorldItem.df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})

WorldItem.df = pd.merge(WorldItem.df, df_statistics, how='outer', on=['MAC'])
WorldItem.df = WorldItem.df.fillna(0)

# Criando arquivo .csv
WorldItem.df.to_csv(
    path_or_buf=os.getenv('DIR_DATA'),
    sep=';',
    columns=['UserID', 'Username', 'IPADDRESS', 'MAC', 'Status', 'AP_ID',
             'AP_NAME', 'RF/WLAN', 'BAND', 'Type', 'RX/TX', 'RSSI', 'VLAN',
             'SSID', '@timestamp-py', "PCKT_SENT", "PCKT_RECEIVED", "BYTES_SENT",
             "BYTES_RECEIVED", "WID_RATE_SENT", "WID_RATE_RECEIVED",
             "TRIGGER_R_TOTAL", "TRIGGER_R_FAILED", "STA_POWER_SAVE"],
    index_label='index',
    line_terminator='\n'
)
