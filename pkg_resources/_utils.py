from dotenv import load_dotenv
import time
import os

load_dotenv()


global WorldItem


class WorldItem:

    timestamp = time.strftime("""%Y-%m-%dT%H:%M:%S%z""")

    regx_mac = '^([0-9A-Fa-f]{4}[:-])'
    regx_userid = '^\s([\d]{1,4})'

    lista_stations = []
    lista_users = []
    lista_mac = []


global AccessControllers


class AccessControllers:

    AC6005 = {
        'device_type': 'huawei',
        'host': os.getenv('HOST'),
        'username': os.getenv('USUARIO'),
        'password': os.getenv('PASSWORD'),
        'global_delay_factor': 1.0,
    }


# global lista_de_dispositivos

# lista_de_dispositivos = []
# lista_de_dispositivos = [AccessControllers.AC6005]

lista_de_comandos = ['display access-user', 'display station all']
