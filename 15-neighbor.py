#
#Access Controller Huawe AC6005 V200R019C00SPC500,
#
#['MAC']
#
#
#
#
#Bibliotecas necessárias
import time
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from netmiko import ConnectHandler
import netmiko
import re
import os
load_dotenv()

start = time.time()
timestamp_data = datetime.now()
timestamp = timestamp_data.strftime('%d/%m/%Y %H:%M')


mac_list = pd.read_csv('mac_list.csv')
mac_list = str(mac_list)
print(mac_list.split('\n'))
for mac in mac_list.split('\n'):
    print(mac[-14::])

dispositivo = {
    'device_type': 'huawei',
    'host': '172.17.1.150',
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 0.1,
}

connection = ConnectHandler(**dispositivo)
connection.enable()

command = 'display station neighbor sta-mac '
outputA = connection.send_command(command)
outputB = str(outputA)
output = outputA

with open('neighbor.csv', 'a') as arquivo:

    for mac in mac_list.split('\n'):
        print(command+mac[-14::])
        outputMac = connection.send_command(command+mac[-14::])
        outputMac = outputMac.split('\n')

        for lineInOutputMac in outputMac:
            if re.search('^([0-9A-Fa-f]{4}[:-])', str(lineInOutputMac)[:6]) is None:
                pass
            else:
                arquivo.write(str(lineInOutputMac)+'      '+mac[-14::]+'\n')

connection.disconnect()

print(output)

#%%
