from requests_huawei.display_station_all import output
from utils.funcoes import (limpar_output)

regx = '^([0-9A-Fa-f]{4}[:-])'

limpar_output(output, regx)

lista_stations = limpar_output(output, regx)
