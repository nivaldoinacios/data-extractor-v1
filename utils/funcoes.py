from .world_itens import (re, timestamp)


def limpar_access_user(output):
    output = output.split('\n')
    result = []
    for line in output:
        if re.search('^\s([\d]{1,4})', str(line)) is None:
            pass
        else:
            result.append(line + ' ' + timestamp + '\n')
    return result


def limpar_display_stations(output):
    output = output.split('\n')
    result = []
    for line in output:
        if re.search('^([0-9A-Fa-f]{4}[:-])', str(line)[:6]) is None:
            pass
        else:
            result.append(line + ' ' + timestamp + '\n')
    return result


def gerar_lista_mac(lista):
    result = []
    for line in lista:
        result.append(line[:14])
    return result
