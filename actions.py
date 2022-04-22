from utils import *
import os

connection = ConnectHandler(**AccessControllers.AC6005,
                            conn_timeout=60)
connection.enable()

command = 'display access-user'
output = connection.send_command(command,
                                 read_timeout=30)

WorldItem.lista_users = limpar_output(
    output,
    WorldItem.regx_userid
)

WorldItem.lista_users = separar_campos(
    WorldItem.lista_users
)

time.sleep(1)

command = 'display station all'
output = connection.send_command(command)

WorldItem.lista_stations = limpar_output(
    output,
    WorldItem.regx_mac
)

WorldItem.lista_stations = separar_campos(
    WorldItem.lista_stations
)


command = 'display station statistics sta-mac '

WorldItem.lista_mac = gerar_lista_mac(
    WorldItem.lista_stations
)

for mac in WorldItem.lista_mac:
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

    WorldItem.lista_statistics.append(output)


connection.disconnect()

#%%
