from netmiko.huawei import HuaweiTelnet
import os

AC6005 = {
    'device_type': 'huawei',
    'host': os.getenv('HOST'),
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 1.0,
}

connection = HuaweiTelnet(**AC6005)

command = 'display access-user'
output = connection.send_command(command)


# limpar_access_user(output)
#
# lista_users = limpar_access_user(output)

# print(lista_users)

#%%
