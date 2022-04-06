from netmiko.huawei import HuaweiTelnet
from etl import (limpar_output,
                 separar_campos,
                 gerar_lista_mac)
from pkg_resources import (
    WorldItem,
    AccessControllers,
)

controladora_bsb = AccessControllers.AC6005


class actionsHuawei:
    def __init__(self):
        self.connection = HuaweiTelnet(**controladora_bsb)

    def display_access_users(self):
        command = 'display access-user'
        output = self.connection.send_command(command)
        # self.connection.disconnect()

        WorldItem.lista_users = limpar_output(
            output,
            WorldItem.regx_userid
        )
        return WorldItem.lista_users

#%%
