#Este programa consulta informações dos usuarios conectados na REDE através do Dispositivo;
#Access Controller Huawe AC6005 V200R019C00SPC500,
#E grava essas inforções em um arquivo .csv; nas colunas
#['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type', 'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID', 'DATA', 'HORA']
#
#comando de referencia: display station all
#
#
#Bibliotecas necessárias
import time
from datetime import datetime
from dotenv import load_dotenv
from netmiko import ConnectHandler
import netmiko
import re
import os

load_dotenv()

timestamp_data = datetime.now()
timestamp = timestamp_data.strftime('%d/%m/%Y %H:%M')


switch_1 = {
    'device_type': 'huawei',
    'host': os.getenv('HOST'),
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 0.1,
}

start = time.time()

connection = ConnectHandler(**switch_1)
connection.enable()
command = 'display station all'

outputA = connection.send_command(command)
outputB = str(outputA)
output = outputA

connection.disconnect()

print(output)

with open('stations.csv', 'w') as arquivo:
    output = output.split('\n')

    for valor in output:
        if re.search('^([0-9A-Fa-f]{4}[:-])', str(valor)[:6]) is None:
            pass
        else:
            arquivo.write(str(valor) + ' ' + timestamp + '\n')

#%%
