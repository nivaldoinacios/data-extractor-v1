import time
import re


global timestamp
global Lista
global Regx


timestamp = time.strftime("""%Y-%m-%dT%H:%M:%S%z""")


class Regx:
    mac = '^([0-9A-Fa-f]{4}[:-])'
    userid = '^\s([\d]{1,4})'


class Lista:

    stations = []
    users = []
    mac = []
    statistics = []


def limpar_output_tabela(output, regx):
    output = output.split('\n')
    result = []

    for line in output:

        if re.search(regx, str(line)) is None:
            pass
        else:
            result.append(line + ' ' + timestamp + '\n')

    return result


def separar_campos_tabela(lista):
    result = []

    for line in lista:
        lista = str(lista)

        line = line.strip()

        line = line.split()

        result.append(line)

    return result


# gera uma lista mac se a primeira coluna do output
# (modelo tabela) for de endereços MAC.
def gerar_lista_mac(lista):
    result = []

    for line in lista:
        result.append(line[0])

    return result
