import numpy as np

m1 = 1
m2 = -1
M = 0

def seleciona_ms(m1, m2, M):
    # Acha todos os valores que podem ser usados na soma
    m = [m1, m2]
    valores = []

    menor = min(m)
    valores.append(menor)

    while menor < max(m):
        menor += 1
        valores.append(menor)

    # Cria as listas para fazer as combinações
    tam = len(valores)

    lista1 = []
    lista2 = []
    lista3 = []
    ms = []

    for i in range(tam):
        lista1.append([valores[i]]*tam)
        lista2.append(valores)

    lista1 = np.array(lista1)
    lista1 = lista1.flatten()

    lista2 = np.array(lista2)
    lista2 = lista2.flatten()

    # Soma todas as combinações possíveis e seleciona as que resultam no valor M permitido
    for i in range(len(lista1)):
        soma = lista1[i] + lista2[i]
        lista3.append(soma)
        if soma == M:
            ms.append([lista1[i], lista2[i]])

    return ms