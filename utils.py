from netmiko.huawei import HuaweiTelnet
from pkg_resources import (
    AccessControllers,
    WorldItem,
    re,
)


def limpar_output(output, regx):
    output = output.split('\n')
    result = []

    for line in output:

        if re.search(regx, str(line)) is None:
            pass
        else:
            result.append(line + ' ' + WorldItem.timestamp + '\n')

    return result


def separar_campos(lista):
    result = []

    for line in lista:
        lista = str(lista)

        line = line.strip()

        line = line.split()

        result.append(line)

    return result


def gerar_lista_mac(lista):
    result = []

    for line in lista:
        result.append(line[0])

    return result


# rever o nome do dispositivo e forma de conexao -> 'issue_1'
# criar um metodo para criar um objeto de conexao com o dispositivo


class fluxoHuawei:
    # issue_1
    def __init__(self):
        pass

    @staticmethod
    def display_access_users():

        connection = HuaweiTelnet(**AccessControllers.AC6005)
        command = 'display access-user'
        output = connection.send_command(command)

        WorldItem.lista_users = limpar_output(
            output,
            WorldItem.regx_userid
        )

        WorldItem.lista_users = separar_campos(
            WorldItem.lista_users
        )

        connection.disconnect()

        return WorldItem.lista_users

    @staticmethod
    def display_station_all():

        connection = HuaweiTelnet(**AccessControllers.AC6005)
        command = 'display station all'
        output = connection.send_command(command)

        WorldItem.lista_stations = limpar_output(
            output,
            WorldItem.regx_mac
        )

        WorldItem.lista_stations = separar_campos(
            WorldItem.lista_stations
        )

        connection.disconnect()

        return WorldItem.lista_stations
