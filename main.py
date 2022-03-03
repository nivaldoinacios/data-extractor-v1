import netmiko
from netmiko import ConnectHandler
import time
import re

switch_1 = {
    'device_type': 'huawei',
    'host': '172.17.1.150',
    'username': 'netmiko',
    'password': '#Roost2021!',
    'global_delay_factor': 0.1,
}
start = time.time()

connection = ConnectHandler(**switch_1)
connection.enable()
command = 'display access-user'

outputA = connection.send_command(command)
outputB = str(outputA)
output = outputA

connection.disconnect()

print(output)

with open('usuarios.csv', 'w') as arquivo:
    output = output.split('\n')

    for valor in output:
        if re.search('[^\s]([\d]{1,4})', str(valor)) is None:
            pass
        else:
            arquivo.write(str(valor)+'\n')