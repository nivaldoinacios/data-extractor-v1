#
from netmiko import ConnectHandler
import netmiko

#
from datetime import datetime
import time

#
import re
import os
#
from dotenv import load_dotenv

load_dotenv()

timestamp_data = datetime.now()
timestamp = timestamp_data.strftime('%d/%m/%Y %H:%M')


switch_1 = {
    'device_type': 'huawei',
    'host': '172.17.1.150',
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
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

with open('PATH_DIS_ACC_USERS', 'w') as arquivo:
    output = output.split('\n')

    for valor in output:
        if re.search('^\s([\d]{1,4})', str(valor)) is None:
            pass
        else:
            arquivo.write(str(valor) + ' ' + timestamp + '\n')
