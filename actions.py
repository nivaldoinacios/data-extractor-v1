import re
import os
from dotenv import load_dotenv
from netmiko import ConnectHandler

load_dotenv()

lista_mac = ['00d7-6d3b-dc6f', '2a87-d116-a3b9', '2ac6-e8b9-3672', '36c6-b432-42e2', '56e3-caef-b634', '5ccd-5bf3-c091',
             '5ccd-5bf3-c0b9', '5ccd-5bf3-c58c', '5e79-0a7e-90b8', '60ab-67c4-61d0', '687d-6bca-12ad', '8056-f2f2-1ae3',
             'a483-e73f-ec23', 'bab2-c64f-295d', 'dc53-600d-abfb', 'f0d7-aaec-18d7']

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
output = connection.send_command(command)


print(output)

lista_mac = ['00d7-6d3b-dc6f', '2a87-d116-a3b9', '2ac6-e8b9-3672', '36c6-b432-42e2', '56e3-caef-b634', '5ccd-5bf3-c091',
             '5ccd-5bf3-c0b9', '5ccd-5bf3-c58c', '5e79-0a7e-90b8', '60ab-67c4-61d0', '687d-6bca-12ad', '8056-f2f2-1ae3',
             'a483-e73f-ec23', 'bab2-c64f-295d', 'dc53-600d-abfb', 'f0d7-aaec-18d7']

stations_statistics = []
for mac in lista_mac:
    print(command + mac)
    outputMac = connection.send_command(command + mac)
    outputMac = outputMac.split('\n')

    for line in outputMac:
        stations_statistics.append(line)

    print(stations_statistics)

connection.disconnect()

