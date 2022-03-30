import get_users_and_stations
import pandas as pd
import os


df_users = pd.read_csv(os.getenv('dir_users'), delim_whitespace=True)
df_users.columns = ["UserID", "Username", "IPADDRESS", "MAC",
                    "Status", "@timestamp-py"]

df_stations = pd.read_csv(os.getenv('dir_stations'), delim_whitespace=True)
df_stations.columns = ['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
                       'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID', "@timestamp-py"]

df_users_stations = pd.merge(df_users, df_stations, on=['MAC'])
df_users_stations = df_users_stations.drop(columns=['IPADDRESS_x', '@timestamp-py_y'])

# metodo para imprimir o dataframe em .csv
# INDEX ELASTIC
# MÉTODO TEMPORARIO
# @cria um arquivo json
# doc = df_users_stations.to_json('doc.json', orient='columns')
# @cria uma variavel q recebe o dataframe convertido em json
# doc = df_users_stations.to_json(orient='columns')
# #####@Index, auto id,
# resp = es.index(index="test-index", document=doc)
# print(resp['result'])


# %%
