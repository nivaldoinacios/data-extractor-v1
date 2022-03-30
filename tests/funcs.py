output = output.split('\n')
lista = []
for line in output:
    if re.search('^\s([\d]{1,4})', str(line)) is None:
        pass
    else:
        lista.append(line + ' ' + timestamp + '\n')