import operacoes
import sympy as sp

# | j1, j2, m1, m2 >, onde m = -j, -j+1, ..., 0 , ..., j-1, j

# J = j1+j2, j1+(j2-1), ..., |j1-j2|

# J(-) |k,j,m> = h sqrt(j(j+1) - m(m-1)) |k,j,m-1>
# J(+) |k,j,m> = h sqrt(j(j+1) - m(m+1)) |k,j,m+1>

# Recebe os momentos individuais
j1, j2 = 1, 1

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
m1 = [i for i in range(-j1, j1+1)]
m2 = [i for i in range(-j2, j2+1)]

# Calcula os possíveis valores J do momento resultante
J = [j1-val for val in m2]

# Calcula os possíveis valores M do momento resultante
M = list(set(J + [-i for i in J]))
M.sort()

# Conjunto completo de todas as equações
conjunto = []

# Armazena exclusivamento os coeficientes
coeficientes = []

# | J=2, M=2 > = | j1=1, j2=1 ; m1=1, m2=1 >
""" 
Cada elemento segue como o modelo da equação acima, 
salvo que o primeiro elemento de cada array possui
armazenado o respectivo coeficiente.
"""

tam = len(M) if len(M) % 2 == 0 else len(M) - 1

for j in range(len(J)):
    # Armazena todas as equações de um dado subespaço
    equacoes = []

    if j == 0:
        equacoes.append([[1, max(J), min(M)],
                        [[1, j1, j2, min(m1), min(m2)]]])
    else:
        equacoes.append(operacoes.muda_subespaco(conjunto[j-1]))
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