from netmiko import ConnectHandler
from pkg_rsrcs import (
    AccessControllers,
    WorldItem,
    threading,
    time,
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


# def post_data():
#     print(f'Iniciando o post dos dados {time.strftime("%H:%M:%S")}')
#
#     try:
#         with open(os.getenv('dir_users_stations'), 'r') as f:
#             reader = csv.DictReader(f, delimiter=';')
#             helpers.bulk(WorldItem.es, reader, index='fluxo')
#
#             time.sleep(1)
#
#             f.close()
#     except Exception as e:
#         print(f'Erro ao executar o post dos dados')
#
#     print(f'Post de dados concluido: {time.strftime("%H:%M:%S")}')


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


# rever o nome do dispositivo e forma de conexao -> 'issue_1'
# criar um metodo para criar um objeto de conexao com o dispositivo


class fluxoHuawei:
    # issue_1
    def __init__(self):
        pass

    # @staticmethod
    # def display_access_users():
    #
    #     connection = ConnectHandler(**AccessControllers.AC6005)
    #     command = 'display access-user'
    #     output = connection.send_command(command)
    #
    #     WorldItem.lista_users = limpar_output(
    #         output,
    #         WorldItem.regx_userid
    #     )
    #
    #     WorldItem.lista_users = separar_campos(
    #         WorldItem.lista_users
    #     )
    #
    #     connection.disconnect()
    #
    #     return WorldItem.lista_users

    # @staticmethod
    # def display_station_all():
    #
    #     connection = ConnectHandler(**AccessControllers.AC6005)
    #     command = 'display station all'
    #     output = connection.send_command(command)
    #
    #     WorldItem.lista_stations = limpar_output(
    #         output,
    #         WorldItem.regx_mac
    #     )
    #
    #     WorldItem.lista_stations = separar_campos(
    #         WorldItem.lista_stations
    #     )
    #
    #     connection.disconnect()
    #
    #     return WorldItem.lista_stations

    @staticmethod
    def get_users_stations():

        connection = ConnectHandler(**AccessControllers.AC6005,
                                    conn_timeout=60)
        connection.enable()

        command = 'display access-user'
        output = connection.send_command(command,
                                         read_timeout=30)

        WorldItem.list_users = limpar_output(
            output,
            WorldItem.regx_userid
        )

        WorldItem.list_users = separar_campos(
            WorldItem.list_users
        )

        time.sleep(1)

        command = 'display station all'
        output = connection.send_command(command)

        WorldItem.list_stations = limpar_output(
            output,
            WorldItem.regx_mac
        )

        WorldItem.list_stations = separar_campos(
            WorldItem.list_stations
        )

        connection.disconnect()

        return WorldItem.list_users, WorldItem.list_stations
