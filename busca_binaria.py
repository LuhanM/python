def busca(lista, x):
    primeiro = 0
    ultimo = len(lista) - 1 

    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        print(str(meio))
        if lista[meio] == x:
            return meio
        else:
            if x < lista[meio]: 
                ultimo = meio - 1
            else:
                primeiro = meio + 1

    return False

def busca_recursiva(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max-min)//2

    if lista[meio] > elemento:
        return busca_recursiva(lista, elemento, min, meio-1)
    elif lista[meio] < elemento:
        return busca_recursiva(lista, elemento, meio + 1, max)
    else:
        return meio

