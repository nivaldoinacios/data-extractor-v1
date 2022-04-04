from requests_huawei.display_station_all import output
from utils.funcoes import (limpar_output, separar_campos)

regx = '^([0-9A-Fa-f]{4}[:-])'

# limpar_output(output, regx)

lista_stations = limpar_output(output, regx)

# separar_campos(lista_stations)

lista_stations = separar_campos(lista_stations)
