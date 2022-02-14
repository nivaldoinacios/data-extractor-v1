import netmiko
from netmiko import ConnectHandler
import time

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

#with open('mapacalor.txt', 'w') as arquivo:
#    for valor in output:
#        arquivo.write(str(valor))
with open('mapacalor.csv', 'w') as arquivo:
    for valor in output:
        arquivo.write(str(valor))
