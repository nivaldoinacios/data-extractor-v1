AC6005 = {
    'device_type': 'huawei',
    'host': '172.17.1.150',
    'username': 'netmiko',
    'password': '#Roost2021!',
    'global_delay_factor': 0.1,
}

from utils.world_itens import *
from netmiko.huawei import HuaweiTelnet
load_dotenv()



start = time.time()

connection = HuaweiTelnet(**AC6005)
connection.enable()

command = 'display access-user'

outputA = connection.send_command(command)
outputB = str(outputA)
output = outputA

#output[303:] essa posição imprime sem o cabeçalho
print(output)