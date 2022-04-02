import sympy as sp
from sympy.solvers.solveset import linsolve

def calcula_possiveis_m_iniciais(j):
    m = []
    m_i = j

    while m_i >= -j:
        m.append(m_i)
        m_i = m_i - 1

    return m

def eleva(ket, ket_somado=False):
    # Verifica se está somando o ket do lado esquerdo da igualdade

    #print(ket)

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

# Acha os ms possíveis de um estado na troca se subespaço
def seleciona_ms(m1, m2, M):
    ms = []

    for i in range(len(m1)):
        for j in range(len(m2)):
            if m1[i]+m2[j] == M:
                ms.append([m1[i], m2[j]])

    return ms

def muda_subespaco(eq1, eq2, cont):
    # Primeira troca de subespaço
    if cont == 0:
        eq_ref = eq1[1]

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
        encontramos que beta = - (c1/c2)*alpha e que alpha = c2/sqrt(c2^2 + c1^2). 
        """
        alpha = c2/sp.sqrt(c2**2 + c1**2)
        beta = - (c1/c2) * alpha

        eq_ref[0][1] -= 1
        eq_ref[1][0][0] = alpha
        eq_ref[1][1][0] = beta

        return eq_ref

def muda_subespaco2(conj, j1, j2, m1, m2):
    # Verifica qual em qual subespaço vai chegar
    J = j1 + j2 - len(conj)
    M = -J

    #print('J = {}'.format(J))

    # Possíves ms do novo subespaço
    pms = seleciona_ms(m1, m2, M)

    #print('pms = {}'.format(pms))

    # O coeficiente do ket |J,J> no ket |j1, j2; m1=j1, m2=J-j1> é sempre escolhido para ser real e positivo
    # Garante que a ordem dos pares em 'pms' siga a regra acima
    condicao_m2 = J-j1
    #print(pms)
    #print('condicao_m2 = {} \n'.format(condicao_m2))

    '''
    posicao = pms.index([0, -J])

    if posicao != 0:
        novo_pms = [pms[posicao]]
        for i in range(len(pms)-1):
            condicao_nova = condicao_m2 + i+1
            posicao_nova = pms.index([j1 - i-1, condicao_nova])
            novo_pms.append(pms[posicao_nova])
    else:
        novo_pms = pms
    '''


    # Compara cada par [m1, m2] com os pares possíveis na troca de subespaço
    comparacao = []

    for i in range(len(conj)):
        sub_comparacao = []
        conj_ref = conj[i]

        # Armazena todos pares [m1, m2] de cada equação de estado de um subespaço
        lista = []
        for i in range(len(conj_ref)):
            sub_lista = []
            for j in range(len(conj_ref[i][1])):
                sub_lista.append(conj_ref[i][1][j][3:])
            lista.append(sub_lista)

        '''
        Compara cada par [m1, m2] das equações do subespaço a que 'comparacao' se refere
        com os pares armazenados em 'pms'. Para cada par que não esteja presente em 'pms',
        a equação ganha um ponto. A equação escolhida para representar o novo subespaço vai ser
        aquela que tiver 0 pontos, ou seja, a que só tiver pares correspondentes com 'pms'.
        Vale ressaltar que o número de pares de uma equação é menor ou igual ao tamanho de 'pms'.
        Em outras palavras, uma equação pode ter um número menor de termos do que todos os pares de
        possíveis ms.
        '''

        for i in range(len(lista)):
            sub_comparacao.append(0)
            for j in range(len(lista[i])):
                if not(lista[i][j] in pms):
                    sub_comparacao[i] += 1

        comparacao.append(sub_comparacao)

    eqs_ref = []
    indices = []
    coefs = []

    for i in range(len(comparacao)):
        sub_coefs = []

        indices.append(comparacao[i].index(0))

        eqs_ref.append(conj[i][indices[i]])

        # Preenche os estados com os termos que faltam.
        #   Ex.: |1, 0> para j1 = j2 = 1 fica faltando o termo 0 * |j1, 2, 0, 0> = 0.

        #print(pms)

        '''Problema aqui!'''
        if len(eqs_ref[i][1]) < len(pms):
            for j in range(len(pms)):
                if not pms[j] == eqs_ref[i][1][j][3:]:
                    eqs_ref[i][1].insert(j, [0, j1, j2, pms[j][0], pms[j][1]]) 
                    break

        # eqs_ref[i-ésima eq][lado da igualdade]
        #       eqs_ref[i-ésima eq][0][elemento do ket]
        #       eqs_ref[i-ésima eq][1][j-ésimo termo][elemento do ket]


        # sub_coefs[coeficiente][número do subespaço][par de ms correspendente]
        for j in range(len(eqs_ref[i][1])):
            sub_coefs.append([eqs_ref[i][1][j][0], eqs_ref[i][0][1], eqs_ref[i][1][j][3:]])

        coefs.append(sub_coefs)

    #print('referencia 1: \n {}'.format(eqs_ref))

    #print('\n')

    # Define os coeficientes do sistema da troca de base a seren determinados (equivalentes a c1, c2, ..., cn)
    a, b, c, d, e, f = sp.symbols('a, b, c, d, e, f')

    num_variaveis = 6

    # Cria a matriz preliminar que representa o sistema
    linhas = []
    for i in range(num_variaveis-1):
        linhas.append([0]*(num_variaveis+1))

    for i in range(len(pms)-1):
        for j in range(len(pms)):
            linhas[i][j] = coefs[i][j][0]
            #pass

    #print(linhas)

    # Cria a matriz SymPy que representa o sistema
    Matriz = sp.Matrix(linhas)

    # Cria o sistema com base na matriz 'Matriz'
    system = A, x = Matriz[:, :-1], Matriz[:, -1]

    # Resolve o sistema
    r = linsolve(system, a, b, c, d, e, f)

    #print(r)

    '''
    A equação de normalização é do tipo |a1|^2 + |a2|^2 + ... + |an|^2 = 1. Podemos subtrair 1 de
    ambos os lados da equação e com isso surge um termo -1 no lado esquerdo da igualdade. Na forma como
    estou desenvolvendo aqui, estou usando de funções do SymPy que consideram sempre o lado
    direito da igualdade como 0, por isso essa pequena manipulação na equação. Isso também explica
    o motivo de inicializar a 'eq_normalizacao' com o valor -1.
    '''
    eq_normalizacao = -1
    for i in range(len(pms)):
        eq_normalizacao += r.args[0][i]**2

    #print(eq_normalizacao)
    #print(r)
    #print(r.args[0][0])

    # Analisa o sinal do primeiro termo da solução
    sinal = str(r.args[0][0])
    correcao = -1 if sinal[0] == '-' else 1
    #print('Valor de sinal[0] = {}'.format(sinal[0]))
    #print('Valor de correcao = {}'.format(correcao))
    #print(r.args[0][len(pms)-1])

    # Resolve a equação de normalização com base na solução do sistema
    s = sp.solve(eq_normalizacao, r.args[0][0]*correcao)
    #print('Valor de s = {}'.format(s))

    # Seleciona apenas o coeficiente positivo
    coef = max(s)
    
    # Calcula os coeficientes de Clabsh-Gordan e monta o ket da nova base
    CG = []
    novo_ket = [[1, J, M], []]

    for i in range(len(pms)):
        CG.append(r.args[0][i]/r.args[0][0] * coef)
        novo_ket[1].append([CG[i], j1, j2, pms[i][0], pms[i][1]])
        
    return novo_ket



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

