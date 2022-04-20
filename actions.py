import re
import os
from dotenv import load_dotenv
from netmiko import ConnectHandler
from utils import gerar_lista_mac, fluxoHuawei, WorldItem

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
    output = output.replace(' ', '')
    output = output.replace('Packetssenttothestation:', '')
    output = output.replace('Packetsreceivedfromthestation:', '')
    output = output.replace('Bytessenttothestation:', '')
    output = output.replace('Bytesreceivedfromthestation:', '')
    output = output.replace('Wirelessdataratesenttothestation(kbps):', '')
    output = output.replace('Wirelessdataratereceivedfromthestation(kbps):', '')
    output = output.replace('Triggerroamtotal:', '')
    output = output.replace('Triggerroamfailed:', '')
    output = output.replace('STApowersavepercent:', '')
    output = output.split('\n')

    stations_statistics.append(output)

    print(stations_statistics)

connection.disconnect()

# %%