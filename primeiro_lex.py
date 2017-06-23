def primeiro_lex(lista):
    result = ''

    for i in lista:
        if result == '' or i < result:
            result = i
        
    return result