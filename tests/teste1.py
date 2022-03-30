from utils.world_itens import *
from utils.device_list import *

connection = HuaweiTelnet(**AC6005)
connection.enable()

command = 'display access-user'

output = connection.send_command(command)

connection.disconnect()

# output[303:] essa posição imprime sem o cabeçalho
# print(output)

output = output.split('\n')
lista_user = []

for line in output:
    if re.search('^\s([\d]{1,4})', str(line)) is None:
        pass
    else:
        lista_user.append(line + ' ' + timestamp + '\n')

print(lista_user)
