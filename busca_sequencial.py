def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False

# lista = [1,2,3,4,5,6]
# print(busca(lista, 10))

# lista = [1,2,3,9,4,5,6]
# print(busca(lista, 9))