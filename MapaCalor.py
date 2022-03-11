# Carrega pacotes netmiko.
import netmiko
from netmiko import ConnectHandler

# Carrega funcoes de tempo; data e hora.
from datetime import datetime
import time

# Carrega, respectivamente, pacotes para expressoes regex e funcoes do sistema operacional.
import re
import os
# Carrega o pacote que permite usarmos '.env' em python.
from dotenv import load_dotenv

load_dotenv()

timestamp = datetime.now()
timestamp = timestamp.strftime('%d/%m/%Y %H:%M')


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
command = 'display station all'

outputA = connection.send_command(command)
outputB = str(outputA)
output = outputA

connection.disconnect()

print(output)

with open(os.getenv('PATH_DIS_STATION'), 'w') as arquivo:
    output = output.split('\n')

    for valor in output:
        if re.search('^([0-9A-Fa-f]{4}[:-])', str(valor)[:6]) is None:
            pass
        else:
            arquivo.write(str(valor) + ' ' + timestamp + '\n')
#%%
