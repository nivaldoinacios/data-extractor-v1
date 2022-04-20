import re
import os
from dotenv import load_dotenv
from netmiko import ConnectHandler
from etl import WorldItem

fluxoHuawei.display_station_all()

lista_mac = gerar_lista_mac(WorldItem.list_stations)

load_dotenv()

dispositivo = {
    'device_type': 'huawei',
    'host': '172.17.1.150',
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 0.1,
}

connection = ConnectHandler(**dispositivo)
connection.enable()

command = 'display station statistics sta-mac '


stations_statistics = []

for mac in lista_mac:

# criar função para output

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

    stations_statistics.append(output)

    print(stations_statistics)

connection.disconnect()

# %%