import netmiko
from netmiko import ConnectHandler
import time
import re

switch_1 = {
    'device_type':'huawei',
    'host':'172.17.1.150',
    'username':'netmiko',
    'password': '#Roost2021!',
    'global_delay_factor':0.1,
}
start = time.time()

connection = ConnectHandler(**switch_1)
connection.enable()
command = 'display station all'

outputA= connection.send_command(command)
outputB = str(outputA)
output = outputA

connection.disconnect()

print(output)

with open('mapacalor.csv', 'w') as arquivo:
    for valor in output:
        if re.search('^([0-9A-Fa-f]{4}[:-])', str(valor)[:6]) is None:
            pass
        else:
            arquivo.write(str(valor)+'\n')
