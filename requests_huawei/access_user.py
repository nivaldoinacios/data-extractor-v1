from netmiko.huawei import HuaweiTelnet
from requests_huawei.device_list import *

connection = HuaweiTelnet(**AC6005)
connection.enable()

command = 'display access-user'
output = connection.send_command(command)

connection.disconnect()

# limpar_access_user(output)
#
# lista_users = limpar_access_user(output)

# print(lista_users)