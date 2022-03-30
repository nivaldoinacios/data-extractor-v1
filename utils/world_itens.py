# Importa as bibliotecas necessárias para o funcionamento do programa
from dotenv import load_dotenv
import time
import os
import re

load_dotenv()

# variaveis globais

global timestamp
timestamp = time.strftime("""%Y-%m-%d'T'%H:%M:%S%z""")
