from netmiko.huawei import HuaweiTelnet
from device_list import *
# from utils.world_itens import *

connection = HuaweiTelnet(**AC6005)
connection.enable()

command = 'display station all'
output = connection.send_command(command)

connection.disconnect()

# limpar_display_stations(output)
#
# lista_stations = limpar_display_stations(output)

# print(lista_stations)
