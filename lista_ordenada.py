def ordenada(lista: list):
    ultimo_valor = lista[0]
    for i in range(len(lista)):
        if lista[i] < ultimo_valor:
            return False
        ultimo_valor = lista[i]
    return True