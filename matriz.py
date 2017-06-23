def cria_matriz(num_col, num_lin):
    result = []
    for col in range(num_col):
        coluna = [] 
        for lin in range(num_lin):
            coluna.append(0)
        result.append(coluna)
    return result

def multiplica_matriz(m1, m2):
    num_linA = len(m1)
    num_colA = len(m1[0])

    num_linB = len(m2)
    num_colB = len(m2[0])

    result = cria_matriz(num_colA, num_linA)
    for linha in range(num_linA):
        for coluna in range(num_colB):
            for k in range(num_colA):
                result[linha][coluna] += m1[linha][k] * m2[k][coluna]

    return result            



print(cria_matriz(4,4))

print(multiplica_matriz([[2,4],[3,5]] , [[6,8], [7,9]]))

#[[2,4],[3,5]] , [[6,8], [7,9]]