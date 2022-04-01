# Importa funções globais e a lista de dispositivos
from utils.world_itens import *
from device_list import *

# Conexão com o dispositivo e obtenção dos dados
connection = HuaweiTelnet(**AC6005)
connection.enable()

command = 'display access-user'

outputA = connection.send_command(command)
outputB = str(outputA)
output = outputA

# output[303:] essa posição imprime sem o cabeçalho
print(output)

# Criação do arquivo de saída com os dados obtidos
with open(os.getenv('dir_users'), 'w') as arquivo:
    output = output.split('\n')

    for valor in output:
        if re.search('^\s([\d]{1,4})', str(valor)) is None:
            pass
        else:
            arquivo.write(str(valor) + ' ' + timestamp + '\n')

# sleep
time.sleep(0.25)

command = 'display station all'

outputA = connection.send_command(command)
outputB = str(outputA)
output = outputA

connection.disconnect()

print(output)

with open(os.getenv('dir_stations'), 'w') as arquivo:
    output = output.split('\n')

    for valor in output:
        if re.search('^([0-9A-Fa-f]{4}[:-])', str(valor)[:6]) is None:
            pass
        else:
            arquivo.write(str(valor) + ' ' + timestamp + '\n')

# ~transformar em função
