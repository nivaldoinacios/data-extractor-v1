# Package resource API
import os
import io
import re
import time
import inspect
import textwrap
import functools
import itertools
from dotenv import load_dotenv

load_dotenv()


global WorldItens


class WorldItens:

    timestamp = time.strftime("""%Y-%m-%dT%H:%M:%S%z""")

    regx_mac = '^([0-9A-Fa-f]{4}[:-])'
    regx_userid = '^\s([\d]{1,4})'

    lista_stations = []
    lista_users = []


global AccessControllers


class AccessControllers:

    AC6005 = {
        'device_type': 'huawei',
        'host': os.getenv('HOST'),
        'username': os.getenv('USUARIO'),
        'password': os.getenv('PASSWORD'),
        'global_delay_factor': 0.5,
    }
