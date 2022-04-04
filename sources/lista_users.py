from requests_huawei.access_user import output
from utils.funcoes import (limpar_output, separar_campos)

regx = '^\s([\d]{1,4})'

# limpar_output(output, regx)

lista_users = limpar_output(output, regx)

# separar_campos(lista_users)

lista_users = separar_campos(lista_users)
