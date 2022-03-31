from .world_itens import (re, timestamp)


def limpar_output(output):

    output = output.split('\n')
    result = []

    for line in output:

        # output = output.split('\n')

        if re.search('^\s([\d]{1,4})', str(line)) or re.search('^([0-9A-Fa-f]{4}[:-])', str(line)[:6]) is None:
            pass
        else:
            result.append(line + ' ' + timestamp + '\n')

    return result
