from utils.funcoes import (limpar_access_user)
from requests_huawei.access_user import output

limpar_access_user(output)

lista_users = limpar_access_user(output)

print(lista_users)
