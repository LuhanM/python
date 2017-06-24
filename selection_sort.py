def ordena(lista):
    
    fim = len(lista)
    for i in range( fim - 1):
        posicao_do_minimo = i
        for x in range(i+1, fim):
            if lista[x] < lista[posicao_do_minimo]:
                posicao_do_minimo = x
        
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

    return lista


lista = [10,9,8,7,6,5,4,3,2,1,0]
print(ordena(lista))