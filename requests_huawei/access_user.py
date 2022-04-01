from netmiko.huawei import HuaweiTelnet
from device_list import *
# from utils.world_itens import *

connection = HuaweiTelnet(**AC6005)
connection.enable()

command = 'display access-user'
output = connection.send_command(command)

connection.disconnect()

# limpar_access_user(output)
#
# lista_users = limpar_access_user(output)

# print(lista_users)
