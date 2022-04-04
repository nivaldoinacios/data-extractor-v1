from dotenv import load_dotenv
import os

load_dotenv()

# Lista de dispositivos
# global dispositivos_huawei
#
# dispositivos_huawei = []
# dispositivos_cisco = []
# dispositivos_aruba = []
# dispositivos_extreme = []
# dispositivos_alcatel = []
# dispositivos_avaya = []

global AC6005

AC6005 = {
    'device_type': 'huawei',
    'host': os.getenv('HOST'),
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 0.5,
}

