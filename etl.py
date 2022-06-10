from netmiko import ConnectHandler
from dotenv import load_dotenv
from utils import *
import pandas as pd
import os

load_dotenv()

AC6005 = {
    'device_type': 'huawei',
    'host': os.getenv('HOST'),
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 1.0,
}


# conecta no dispositivo
connection = ConnectHandler(**AC6005, conn_timeout=60)
connection.enable()

# envia os comandos ao dispositivo
command = 'display access-user'
output = connection.send_command(command)

# trata os dados do output
Lista.users = limpar_output_tabela(
    output,
    Regx.userid
)

Lista.users = separar_campos_tabela(
    Lista.users
)

time.sleep(1)

command = 'display station all'
output = connection.send_command(command)

Lista.stations = limpar_output_tabela(
    output,
    Regx.mac
)

Lista.stations = separar_campos_tabela(
    Lista.stations
)

# gera uma lista MAC, utiliza a lista 'station_all'
command = 'display station statistics sta-mac '

Lista.mac = gerar_lista_mac(
    Lista.stations
)

# envia, recursivamente, o comando para cada MAC da lista
for mac in Lista.mac:
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

    Lista.statistics.append(output)

# encerra a sessão aberta no dispositivo
connection.disconnect()

# print(Lista.statistics)
# print(Lista.stations)
# print(Lista.users)
# print(Lista.mac)

#%%
