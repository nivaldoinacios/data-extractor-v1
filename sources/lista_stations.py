from utils.funcoes import (limpar_display_stations)
from requests_huawei.display_station_all import output

limpar_display_stations(output)

lista_stations = limpar_display_stations(output)

print(lista_stations)
