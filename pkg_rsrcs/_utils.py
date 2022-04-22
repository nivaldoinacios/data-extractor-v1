from elasticsearch import Elasticsearch, helpers
from dotenv import load_dotenv
import threading
import time
import csv
import os
import io
import re

load_dotenv()


global WorldItem


class WorldItem:

    timestamp = time.strftime("""%Y-%m-%dT%H:%M:%S%z""")

    regx_mac = '^([0-9A-Fa-f]{4}[:-])'
    regx_userid = '^\s([\d]{1,4})'

    lista_stations = []
    lista_users = []
    lista_mac = []
    lista_statistics = []

    df = None

    es = Elasticsearch(
        ['http://192.168.10.14:9200'],
        basic_auth=(
            os.getenv('ELK_USERNAME'),
            os.getenv('ELK_PASSWORD'))
    )


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
