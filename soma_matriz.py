def soma_matrizes(m1,m2):
    if len(m1) != len(m2):
        return False
    matriz_somada = m1[:]
    for i in range(len(m1)):
        if len(m1[i]) != len(m2[i]):
            return False
        for j in range(len(m1[i])):
            matriz_somada[i][j] = m1[i][j] + m2[i][j]
    return matriz_somada