def conta_letras(frase, contar="vogais"):
    total_vogais = 0
    total_consoantes = 0
    vogais = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(frase)):
        if (frase[i] != ' ') and (frase[i].lower() in vogais):
            total_vogais += 1
        elif (frase[i] != ' '):
            total_consoantes += 1

    if contar == "vogais":
        return total_vogais
    else:
        return total_consoantes
    
print(conta_letras('programamos em python'))
print(conta_letras('programamos em python', 'vogais'))
print(conta_letras('programamos em python', 'consoantes'))