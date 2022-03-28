import sympy as sp

def calcula_possiveis_m(j):
    m = []
    m_i = j

    while m_i >= -j:
        m.append(m_i)
        m_i = m_i - 1

    return m

def eleva(ket, ket_somado=False):
    # Verifica se está somando o ket do lado esquerdo da igualdade
    if ket_somado:
        coef = ket[0]
        j = ket[1]
        m = ket[2]

        coef = coef * sp.sqrt(j*(j+1)-m*(m+1))

        ket_elev = [coef, j, m+1]
    
    else:
        coef = ket[0]

        if coef == 0:
            return [0]*5

        j1 = ket[1]
        j2 = ket[2]
        m1 = ket[3]
        m2 = ket[4]

        coef1 = coef * sp.sqrt(j1*(j1+1)-m1*(m1+1))
        coef2 = coef * sp.sqrt(j2*(j2+1)-m2*(m2+1))

        if m1 >= j1 and m2 >= j2:
            #print('m1 >= j1 and m2 >= j2')
            ket_elev = []
        elif m1 >= j1:
            #print('m1 >= j1')
            ket_elev = [[0]*5, [coef2, j1, j2, m1, m2+1]]
        elif m2 >= j2:
            #print('m2 >= j2')
            ket_elev = [[coef1, j1, j2, m1+1, m2], [0]*5]
        else:
            #print('ok')
            ket_elev = [[coef1, j1, j2, m1+1, m2], [coef2, j1, j2, m1, m2+1]]

    #print(ket_elev)
    return ket_elev


# Soma termos iguais que resultarem da aplicação do J(+) em cada ket
def soma_kets_iguais(kets):
    while len(kets)>1:
        #print('\n kets:', kets)
        tam = len(kets)
        aux = []
        # Remove kets nulos
        #print('\n kets[1]:', kets[1])
        #kets[1] = list(filter(lambda a: a != [0]*5, kets[1]))
        #print('\n kets[1]:', kets[1])

        for ket in kets[1]:
            #print(ket)
            aux.append(ket[1:])

        for i in range(len(kets[0])):
            #print('i:', i)
            #print('\n kets[0]:', kets[0])
            #print('\n kets[1]:', kets[1], '\n')
            if kets[0][i][0] == 0:
                #print('continue')
                continue

            if kets[0][i][1:] in aux:
                indice = aux.index(kets[0][i][1:])
                kets[0][i][0] += kets[1][indice][0]
                kets[1].pop(indice)
                kets[0] += kets[1]
                kets.pop(1)

        if len(kets) == tam:
            #print(i)
            kets[0] += kets[1]
            kets.pop(1)
            i += 1
            #print(i)

    #print('\n kets:', kets)
    for ket in kets[0]:
        if ket[0] == 0:
            kets[0].pop(kets[0].index(ket))
    
    return kets


# [[1, j, m],[[1, j1, j2, min(m1), min(m2)], [0], [0]]]

def j_mais(eq):
    kets = []
    cont = 1

    for ket in eq:
        if eq.index(ket) == 0:
            kets.append(eleva(ket, ket_somado=True))

        else:
            aux = []
            for kt in ket:
                #print('rodada', cont)
                cont += 1
                aux.append(eleva(kt))
            
            kets.append(aux)

    #print('\n Deu certo')
    """ 
    Se len(kets[1]) > 1, quer dizer que o "levantamento" por meio do J(+)
    resultou em termos (kets) que podem ser somados.
    """
    #print('\n', kets[1])
    #print('len(kets[1]):', len(kets[1]))
    if len(kets[1]) > 1:
        kets[1] = soma_kets_iguais(kets[1])
    #print(kets)

    # Remove kets nulos
    #print('kets[1] antes:', kets[1])
    kets[1] = list(filter(lambda a: a != [0]*5, kets[1][0]))
    #print('kets[1] depois:', kets[1])
    
    # Divide a equação pelo coeficiente do lado esqerdo
    coef = kets[0][0]
    kets[0][0] = 1
    for ket in kets[1]:
        ket[0] /= coef

    return kets

def muda_subespaco(eq):
    eq_ref = eq[1]

    # Lê os coeficientes do lado direito da equação de referência
    c1 = eq_ref[1][0][0]
    c2 = eq_ref[1][1][0]

    """ 
    Dado um novo vetor em um subespaço menor, seus coeficientes alpha e beta
    devem ser tais que |alpha|^2 + |beta|^2 + ... = 1. Podemos convencionar que
    alpha e beta são reais e também que alpha é positivo. Disso, comparamos
    esse novo vetor com um dos vetores do subespaço superior em busca de uma
    dependêncian linear. Com isso, determinamos então os valores de alpha e beta.
    Sendo c1 e c2 os coeficientes do vetor conhecido do subespaço superior,
    encontramos que beta = - (c1/c2) alpha e que alpha = c2/sqrt(c2^2 + c1^2).
    """
    alpha = c2/sp.sqrt(c2**2 + c1**2)
    beta = - (c1/c2) * alpha

    eq_ref[0][1] -= 1
    eq_ref[1][0][0] = alpha
    eq_ref[1][1][0] = beta

    return eq_ref

""" 
eq = [[1, 2, 0], [[sp.sqrt(6)/6, 1, 1, 1, -1], [sp.sqrt(6)/3, 1, 1, 0, 0], [sp.sqrt(6)/6, 1, 1, -1, 1]]]
print('eq1:', eq)

# Exemplo de partida
#eq = [  [1, 2, -2], [  [1, 1, 1, -1, -1]  ]  ]

# Se tudo estiver certo, esses são os cinco passos que devem varrer E(J=2)
eq2 = j_mais(eq)
print('eq2:', eq2)
#eq3 = j_mais(eq2)
#eq4 = j_mais(eq3)
#eq5 = j_mais(eq4)

#print(eq)
#print(eq2)
#print('eq3:', eq3)
#print(eq4)
#print(eq5)
print('\n')
 """

""" 
O programa, naturalmente, deve respeitar a mecânica quântica, de forma que 
a operação abaixo seja proibida, já que m = -j, -j+1, ..., 0 , ..., j-1, j.
Se o código não tiver nenhum filtro para esta ressalva, os coeficientes dos
kets resultantes serão 'nans', o que não faz nenhum sentido físico, matemático,
filosófico, biológico, pscicológico ou o que for (a não ser, é claro, para os
coachs quânticos).
Devo implementar esse cuidado no código principal.

[[1, 1, 0], [[sqrt(2)/2, 1, 1, 1, -1], [-sqrt(2)/2, 1, 1, -1, 1]]]
 """
#eq6 = j_mais(eq5)
#print(eq6)

