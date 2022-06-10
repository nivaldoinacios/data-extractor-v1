from etl import Lista
import pandas as pd

global df_station_all

df_station_all = pd.DataFrame(Lista.stations,
                               columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
                                        'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID',
                                        "@timestamp-py"]
                               )

df_station_all
