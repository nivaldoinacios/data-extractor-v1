# Lista de dispositivos

# importa os modulos necessarios
from utils.world_itens import (load_dotenv, os)
from netmiko.huawei import HuaweiTelnet

# carrega as variaveis de ambiente
# load_dotenv()

# declara as variaveis(dispositivos) como globais
global AC6005

AC6005 = {
    'device_type': 'huawei',
    'host': os.getenv('HOST'),
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 1.0,
}