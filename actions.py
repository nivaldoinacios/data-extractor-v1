from netmiko.huawei import HuaweiTelnet
from etl import (limpar_output,
                 separar_campos,
                 )
from pkg_resources import (
    WorldItem,
    AccessControllers,
)

# rever o nome do dispositivo e forma de conexao -> 'issue_1'
# criar um metodo para criar um objeto de conexao com o dispositivo


class fluxoHuawei:
    # issue_1
    def __init__(self):
        self.connection = HuaweiTelnet(**AccessControllers.AC6005)

    def display_access_users(self):
        command = 'display access-user'
        output = self.connection.send_command(command)

        self.connection.disconnect()

        WorldItem.lista_users = limpar_output(
            output,
            WorldItem.regx_userid
        )

        WorldItem.lista_users = separar_campos(
            WorldItem.lista_users
        )

        return WorldItem.lista_users

    def display_station_all(self):
        command = 'display station all'
        output = self.connection.send_command(command)

        self.connection.disconnect()

        WorldItem.lista_stations = limpar_output(
            output,
            WorldItem.regx_mac
        )

        WorldItem.lista_stations = separar_campos(
            WorldItem.lista_stations
        )

        return WorldItem.lista_stations


#%%
