import operacoes
import sympy as sp
 
# | j1, j2, m1, m2 >, onde m = -j, -j+1, ..., 0 , ..., j-1, j

# J = j1+j2, j1+(j2-1), ..., |j1-j2|

# J(-) |k,j,m> = h sqrt(j(j+1) - m(m-1)) |k,j,m-1>
# J(+) |k,j,m> = h sqrt(j(j+1) - m(m+1)) |k,j,m+1>

# Recebe os momentos individuais
j1, j2 = "2", "2"

# Garante que um j seja semi inteiro quando for o caso
j1 = sp.parse_expr(j1)
j2 = sp.parse_expr(j2)

# Printa os j que estão sendo considerados
print('\n Cálculo dos coeficientes para j1={} e j2={} \n'.format(j1,j2))

""" 
Veja que j1 deve ser maior que j2.
Convenção apenas para os cálculos funcionarem.
O programa precisa garantir isso, não o usuário.
"""
# Garante que j1 > j2
if j2 > j1:
    aux = j1
    j1 = j2
    j2 = aux

# Calcula os m de cada partícula
m1 = operacoes.calcula_possiveis_m_iniciais(j1)
m2 = operacoes.calcula_possiveis_m_iniciais(j2)

# Calcula os possíveis valores J do momento resultante
J = [j1-val for val in m2]

#print(J)

# Calcula os possíveis valores M do momento resultante
M = list(set(J + [-i for i in J]))
M.sort()

#print(M)

# Conjunto completo de todas as equações
conjunto = []

# Armazena exclusivamente os coeficientes
coeficientes = []

# | J=2, M=2 > = | j1=1, j2=1 ; m1=1, m2=1 >
""" 
Cada elemento segue como o modelo da equação acima, 
salvo que o primeiro elemento de cada array possui
armazenado o respectivo coeficiente.
"""

# Verifica se a quantidade de valores possíveis para M (tamanho do array M)
# tam = len(M) if len(M) % 2 == 0 else len(M) - 1
tam = len(M) if len(M) % 2 == 0 else len(M) - 1

# Em casos de soma de j's inteiro com semi-inteiro, também descontamos 1
if type(j1) == sp.core.numbers.Half and type(j1) != type(j2):
    tam -= 1
if type(j2) == sp.core.numbers.Half and type(j2) != type(j1):
    tam -= 1

 
for j in range(len(J)):
    # Armazena todas as equações de um dado subespaço
    equacoes = []

    if j == 0:
        equacoes.append([[1, max(J), min(M)],
                        [[1, j1, j2, min(m1), min(m2)]]])
    else:
        equacoes.append(operacoes.muda_subespaco2(conjunto, j1, j2, m1, m2))

        if conjunto[j-1][0][0][1] == 1:
            #print('conjunto[j-1][0][1] == 1')
            print(equacoes[0])
            conjunto.append(equacoes)
            break

    for i in range(tam):
        print(equacoes[i])
        equacoes.append(operacoes.j_mais(equacoes[i]))
    print(equacoes[i+1], '\n')

    conjunto.append(equacoes)

    tam -= 2
    if tam<=0:
        tam = 1

""" 
print('\n')
equacoes2 = []
equacoes2.append(operacoes.muda_subespaco(equacoes))

for i in range(tam-2):
    print(equacoes2[i])
    equacoes2.append(operacoes.j_mais(equacoes2[i]))
print(equacoes2[i+1])
 """

# [[1, 1, -1], [[sqrt(2)/2, 1, 1, 0, -1], [-sqrt(2)/2, 1, 1, -1, 0]]]
