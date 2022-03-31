import sympy as sp
import operacoes

# Recebe os momentos individuais
j1, j2 = "2", "1"

# Garante que um j seja semi inteiro quando for o caso
j1 = sp.parse_expr(j1)
j2 = sp.parse_expr(j2)

# Printa os j que estão sendo considerados
print('\n Cálculo dos coeficientes para j1={} e j2={} \n'.format(j1,j2))

# Garante que j1 > j2
if j2 > j1:
    aux = j1
    j1 = j2
    j2 = aux

# Calcula os m de cada partícula
m1 = operacoes.calcula_possiveis_m_iniciais(j1)
m2 = operacoes.calcula_possiveis_m_iniciais(j2)

M = 0

# Possíves ms do novo subespaço
pms = operacoes.seleciona_ms(m1, m2, M)

eq2_1 = [[1, 2, -2], [[1, 1, 1, -1, -1]]]
eq2_2 = [[1, 2, -1], [[sp.sqrt(2)/2, 1, 1, 0, -1], [sp.sqrt(2)/2, 1, 1, -1, 0]]]
eq2_3 = [[1, 2, 0], [[sp.sqrt(6)/6, 1, 1, 1, -1], [sp.sqrt(6)/3, 1, 1, 0, 0], [sp.sqrt(6)/6, 1, 1, -1, 1]]]
eq2_4 = [[1, 2, 1], [[sp.sqrt(2)/2, 1, 1, 1, 0], [sp.sqrt(2)/2, 1, 1, 0, 1]]]
eq2_5 = [[1, 2, 2], [[1, 1, 1, 1, 1]]] 

eq1_1 = [[1, 1, -1], [[sp.sqrt(2)/2, 1, 1, 0, -1], [-sp.sqrt(2)/2, 1, 1, -1, 0]]]
eq1_2 = [[1, 1, 0], [[sp.sqrt(2)/2, 1, 1, 1, -1], [-sp.sqrt(2)/2, 1, 1, -1, 1]]]
eq1_3 = [[1, 1, 1], [[sp.sqrt(2)/2, 1, 1, 1, 0], [-sp.sqrt(2)/2, 1, 1, 0, 1]]] 

conj = [[eq2_1, eq2_2, eq2_3, eq2_4, eq2_5], [eq1_1, eq1_2, eq1_3]]

# conj[subespaço][equaçao][lado da igualdade][termo][componentes do termo]

def muda_subespaco2(conj, pms):
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

    return comparacao


print(pms)
print(muda_subespaco2(conj, pms))



