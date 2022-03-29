from netmiko import ConnectHandler
from dotenv import load_dotenv
import time
import re
import os

load_dotenv()

timestamp = time.strftime("""%Y-%m-%d'T'%H:%M:%S%z""")

#Dispostivo
AC6005 = {
    'device_type': 'huawei',
    'host': os.getenv('HOST'),
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 0.1,
}

