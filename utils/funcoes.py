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
        result.append(line[:14])

    return result
