# Importa as bibliotecas necessárias para o funcionamento do programa
from netmiko.huawei import HuaweiTelnet
from dotenv import load_dotenv
import time
import re
import os

load_dotenv()

# variaveis globais

global timestamp
timestamp = time.strftime("""%Y-%m-%d'T'%H:%M:%S%z""")
