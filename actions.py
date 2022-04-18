import re
import os
from dotenv import load_dotenv
from netmiko import ConnectHandler
from utils import gerar_lista_mac, fluxoHuawei, WorldItem

fluxoHuawei.display_station_all()

lista_mac = gerar_lista_mac(WorldItem.list_stations)



load_dotenv()

# definir método para importar lista mac
# lista_mac = ['0045-e269-97bb', '00d7-6d3b-dc6f', '2a87-d116-a3b9', '2ac6-e8b9-3672',
#              '36c6-b432-42e2', '389a-f679-e1bd', '5642-e79d-40e8', '56e3-caef-b634',
#              '5ccd-5bf3-c091', '5ccd-5bf3-c1bd', '5ccd-5bf3-c58c', '5e79-0a7e-90b8',
#              '60ab-67c4-61d0', '6432-a843-f0da', '6616-2ec5-1f96', '7c8b-b531-3c4f',
#              '7e09-131c-a6c6', '8af2-8400-f361', '9e26-b35e-0305', 'a483-e73f-ec23',
#              'a6fd-c54d-712e', 'a816-d031-88c1', 'b6f0-6d6e-e1b6', 'bab2-c64f-295d',
#              'bc6a-d1fb-b822', 'ca01-740a-cbcc', 'dc53-600d-abfb']

dispositivo = {
    'device_type': 'huawei',
    'host': '172.17.1.150',
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 0.1,
}

connection = ConnectHandler(**dispositivo)
connection.enable()

# command = 'display station sta-mac '
command = 'display station statistics sta-mac '
# output = connection.send_command(command)
# print(output)

stations_statistics = []

for mac in lista_mac:
    # print(command + mac)
    output = connection.send_command(command + mac)
    output = output.replace(output[0:78], mac, 1)
    output = output.replace("""------------------------------------------------------------------------------""", '', 1)
    output = output.split('\n')
    stations_statistics.append(output)
    # output = output.split('\n')
    # output = output.split('------------------------------------------------------------------------------')

    # for line in output:
        # if '-' in line:
        #     pass
        # else:
        #     # stations_statistics.insert(0, mac)
        # stations_statistics.append(line)
    # após tratamento regex para remover caracteres redundantes, verificar possição do insert mac

    print(stations_statistics)

connection.disconnect()

# %%
# 268:705