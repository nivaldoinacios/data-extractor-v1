#Bibliotecas necessárias
import time
import numpy as np
import pandas as pd
from io import StringIO
# from ListaMac import mac_list
from datetime import datetime
from dotenv import load_dotenv
from netmiko import ConnectHandler
import netmiko
import re
import os
load_dotenv()

timestamp_data = datetime.now()
timestamp = timestamp_data.strftime('%d/%m/%Y %H:%M')

dispositivo = {
    'device_type': 'huawei',
    'host': os.getenv('HOST'),
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 0.1,
}

start = time.time()

connection = ConnectHandler(**dispositivo)
connection.enable()

command = 'display access-user'
outputA = connection.send_command(command)
outputB = str(outputA)
output = outputA

connection.disconnect()

output = output[303:]
print(output)
type(output)
#%%
# # output = output.split('\n')
# # output.split('\n')
#%%
clean = output.replace('--', '')
clean = clean.replace('                             ', '             ')
clean = clean.split('\n')
clean.pop()
clean.pop()
clean.remove('')
clean

clean = df
df
#%%