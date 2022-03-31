# Importa funções globais e a lista de dispositivos
from utils.world_itens import *
from utils.device_list import *

# global lista_users
# lista_users = []
#
# global lista_stations
# lista_stations = []

# Conexão com o dispositivo e obtenção dos dados
connection = HuaweiTelnet(**AC6005)
connection.enable()


command = 'display access-user'
output = connection.send_command(command)
output = output.split('\n')
# lista_users = []
for line in output:
    if re.search('^\s([\d]{1,4})', str(line)) is None:
        pass
    else:
        lista_users.append(line + ' ' + timestamp + '\n')

# print(lista_users)

command = 'display station all'
output = connection.send_command(command)


output = output.split('\n')
# lista_stations = []
for line in output:
    if re.search('^([0-9A-Fa-f]{4}[:-])', str(line)[:6]) is None:
        pass
    else:
        lista_stations.append(line + ' ' + timestamp + '\n')

# print(lista_stations)

connection.disconnect()
# ~transformar em função
