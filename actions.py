from df_statistics import *
from df_base import *
import pandas as pd

df = pd.merge(df, pd_df, how='outer', on=['MAC'])

print(df)


df.to_csv(
    path_or_buf=os.getenv('dados'),
    sep=';',
    columns=['UserID', 'Username', 'IPADDRESS', 'MAC', 'Status', 'AP_ID',
             'AP_NAME', 'RF/WLAN', 'BAND', 'Type', 'RX/TX', 'RSSI', 'VLAN',
             'SSID', '@timestamp-py', "PCKT_SENT", "PCKT_RECEIVED", "BYTES_SENT",
             "BYTES_RECEIVED", "WID_RATE_SENT", "WID_RATE_RECEIVED",
             "TRIGGER_R_TOTAL", "TRIGGER_R_FAILED", "STA_POWER_SAVE", "BYTES_SENT_CALC"],
    index_label='index',
    line_terminator='\n'
)
