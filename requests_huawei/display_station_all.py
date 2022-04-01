from netmiko.huawei import HuaweiTelnet
from requests_huawei.device_list import *


connection = HuaweiTelnet(**AC6005)
connection.enable()

command = 'display station all'
output = connection.send_command(command)

connection.disconnect()

# limpar_display_stations(output)
#
# lista_stations = limpar_display_stations(output)

# print(lista_stations)
