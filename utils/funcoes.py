from .world_itens import (re, timestamp)


def limpar_output(output, regx):
    output = output.split('\n')
    result = []

    for line in output:

        if re.search(regx, str(line)) is None:
            pass
        else:
            result.append(line + ' ' + timestamp + '\n')

    return result


def gerar_lista_mac(lista):
    result = []

    for line in lista:
        result.append(line[0])

    return result


# Deprecated
# def gerar_lista_mac(lista):
#     result = []
#
#     for line in lista:
#         result.append(line[:14])
#
#     return result


def separar_campos(lista):
    result = []

    for line in lista:
        lista = str(lista)

        line = line.strip()

        line = line.split()

        result.append(line)

    return result

