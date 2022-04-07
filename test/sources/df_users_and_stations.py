from lista_stations import lista_stations
from lista_users import lista_users
import pandas as pd

df_stations = pd.DataFrame(lista_stations, columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
                                                    'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID', "@timestamp-py"])

df_users = pd.DataFrame(lista_users, columns=["UserID", "Username", "IPADDRESS", "MAC",
                                              "Status", "@timestamp-py"])

df = pd.merge(df_users, df_stations, how='outer', on=['MAC'])
df = df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
df = df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
df = df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})

df = df.fillna(0)

df



#%%
