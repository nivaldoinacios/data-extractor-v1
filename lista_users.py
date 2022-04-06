from utils import (limpar_output, separar_campos)
from access_user import output

regx = '^\s([\d]{1,4})'

# limpar_output(output, regx)

lista_users = limpar_output(output, regx)

# separar_campos(lista_users)

lista_users = separar_campos(lista_users)
