import sympy as sp
from sympy.solvers.solveset import linsolve

def printa_latex(eq):
    # Lê J e M no lado esquerdo da equação
    J_lt = eq[0][1]
    M_lt = eq[0][2]

    # Monta o código em LaTeX para o lado esquerdo da equação
    lado_esquerdo = '|' + sp.latex(J_lt) + ';' + sp.latex(M_lt) + '\\rangle' + '='

    # Inicializa a string de todos os termos da equação
    termos = lado_esquerdo

    # Conta quantos termos existem no lado direito da equação
    n_termos = len(eq[1])

    # Cria o código LaTeX para cada termo do lado direito da equação e soma com os anteriores
    for i in range(n_termos):
        CS = eq[1][i][0]
        j1 = eq[1][i][1]
        m1 = eq[1][i][2]
        j2 = eq[1][i][3]
        m2 = eq[1][i][4]

        termo = sp.latex(CS) + '|' + sp.latex(j1) + ',' + sp.latex(m1) + ';' + sp.latex(j2) + ',' + sp.latex(m2) + '\\rangle'

        # Faz a regulagem dos sinais dos coeficientes
        if i == 0:
            termos += termo
        else:
            if CS < 0:
                termos += termo
            else:
                termos += '+' + termo

    return termos
    

def calcula_possiveis_m_iniciais(j):
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
            ket_elev = []
        elif m1 >= j1:
            ket_elev = [[0]*5, [coef2, j1, j2, m1, m2+1]]
        elif m2 >= j2:
            ket_elev = [[coef1, j1, j2, m1+1, m2], [0]*5]
        else:
            ket_elev = [[coef1, j1, j2, m1+1, m2], [coef2, j1, j2, m1, m2+1]]

    return ket_elev


# Soma termos iguais que resultarem da aplicação do J(+) em cada ket
def soma_kets_iguais(kets):
    while len(kets)>1:
        tam = len(kets)
        aux = []

        for ket in kets[1]:
            aux.append(ket[1:])

        for i in range(len(kets[0])):
            if kets[0][i][0] == 0:
                continue

            if kets[0][i][1:] in aux:
                indice = aux.index(kets[0][i][1:])
                kets[0][i][0] += kets[1][indice][0]
                kets[1].pop(indice)
                kets[0] += kets[1]
                kets.pop(1)

        if len(kets) == tam:
            kets[0] += kets[1]
            kets.pop(1)
            i += 1

    for ket in kets[0]:
        if ket[0] == 0:
            kets[0].pop(kets[0].index(ket))
    
    return kets


def j_mais(eq):
    kets = []
    cont = 1

    for ket in eq:
        if eq.index(ket) == 0:
            kets.append(eleva(ket, ket_somado=True))

        else:
            aux = []
            for kt in ket:
                cont += 1
                aux.append(eleva(kt))
            
            kets.append(aux)

    """ 
    Se len(kets[1]) > 1, quer dizer que o "levantamento" por meio do J(+)
    resultou em termos (kets) que podem ser somados.
    """
    
    if len(kets[1]) > 1:
        kets[1] = soma_kets_iguais(kets[1])
    

    # Remove kets nulos
    kets[1] = list(filter(lambda a: a != [0]*5, kets[1][0]))
    
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


def muda_subespaco(conj, j1, j2, m1, m2):
    # Verifica qual em qual subespaço vai chegar
    J = j1 + j2 - len(conj)
    M = -J

    # Possíves ms do novo subespaço
    pms = seleciona_ms(m1, m2, M)

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


    # Verifica se os elementos de 'coefs' estão coerentes em relação ao tamanho
    for i in range(len(coefs)):
        if len(coefs[i]) < len(pms):
            for j in range(len(pms)):
                if not pms[j] == coefs[i][j][2]:
                    coefs[i].insert(j, [0, j1, j2, pms[j][0], pms[j][1]]) 
                    break

    # Define os coeficientes do sistema da troca de base a serem determinados (equivalentes a c1, c2, ..., cn)
    a, b, c, d, e, f, g = sp.symbols('a, b, c, d, e, f, g')
    variaveis = [a, b, c, d, e, f, g]
    num_variaveis = len(variaveis)


    # Cria a matriz preliminar que representa o sistema
    linhas = []
    for i in range(num_variaveis-1):
        linhas.append([0]*(num_variaveis+1))
        

    # Preenche a matriz com os coeficientes
    for i in range(len(pms)-1):
        for j in range(len(pms)):
            linhas[i][j] = coefs[i][j][0]
            #pass


    # Cria a matriz SymPy que representa o sistema
    Matriz = sp.Matrix(linhas)

    # Cria o sistema com base na matriz 'Matriz'
    system = A, x = Matriz[:, :-1], Matriz[:, -1]

    # Resolve o sistema
    r = linsolve(system, a, b, c, d, e, f, g)

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

    # Analisa o sinal do primeiro termo da solução
    sinal = str(r.args[0][0])
    correcao = -1 if sinal[0] == '-' else 1

    # Resolve a equação de normalização com base na solução do sistema
    s = sp.solve(eq_normalizacao, variaveis[len(pms)-1])
    
    # Seleciona apenas o coeficiente positivo e já insere o sinal de correção quando for o caso
    coef = max(s)*correcao
    
    # Calcula os coeficientes de Clabsh-Gordan e monta o ket da nova base
    CG = []
    novo_ket = [[1, J, M], []]

    for i in range(len(pms)):
        CG.append(r.args[0][i]/variaveis[len(pms)-1] * coef)
        novo_ket[1].append([CG[i], j1, j2, pms[i][0], pms[i][1]])
        
    return novo_ket
