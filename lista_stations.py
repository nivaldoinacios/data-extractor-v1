from utils import (limpar_output, separar_campos)
from display_station_all import output

regx = '^([0-9A-Fa-f]{4}[:-])'

# limpar_output(output, regx)

lista_stations = limpar_output(output, regx)

# separar_campos(lista_stations)

lista_stations = separar_campos(lista_stations)
