def menor_nome(nomes):
    result = ''
    for name in nomes:
        if (result == '') or (len(name.strip()) < len(result)):
            result = name.strip()
    return result.capitalize()