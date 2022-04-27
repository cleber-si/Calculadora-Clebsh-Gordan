import operacoes
import sympy as sp

from IPython.display import display, Math
 
# | j1, j2, m1, m2 >, onde m = -j, -j+1, ..., 0 , ..., j-1, j

# J = j1+j2, j1+(j2-1), ..., |j1-j2|

# J(-) |k,j,m> = h sqrt(j(j+1) - m(m-1)) |k,j,m-1>
# J(+) |k,j,m> = h sqrt(j(j+1) - m(m+1)) |k,j,m+1>

def calcula(j1, j2, latex=False):
    limite_subespacos = 7

    # Garante que um j seja semi inteiro quando for o caso
    j1 = sp.parse_expr(j1)
    j2 = sp.parse_expr(j2)

    # Printa os j que estão sendo considerados
    if latex:
        print('\n')
        texto = 'Cálculo dos autoestados para '
        display(Math(sp.latex(texto) + 'j_{1}' + '=' + sp.latex(j1) + sp.latex(' e ') + 'j_{2}' + '=' + sp.latex(j2) + sp.latex(':')))
    else:
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
    J.sort(reverse=True)

    #print(J, '\n')

    # Conjunto completo de todas as equações
    conjunto = []

    # | J=2, M=2 > = | j1=1, j2=1 ; m1=1, m2=1 >
    """ 
    Cada elemento segue como o modelo da equação acima, 
    salvo que o primeiro elemento de cada array possui
    armazenado o respectivo coeficiente.
    """


    # Indica a quantidade de subespaços a serem trabalhados
    tam_J = len(J)

    # Chave para avisar o usuário quando o limite de subespaços for atingido
    aviso = False

    if tam_J > limite_subespacos:
        tam_J = limite_subespacos
        aviso = True

    for j in range(tam_J):
        # Printa o subespaço que está sendo considerado
        if latex:
            texto = 'Subespaço '
            display(Math(sp.latex(texto) + '\\varepsilon' + sp.latex('(J') + '=' + sp.latex(J[j]) + sp.latex(')')))
        else:
            print('Subespaço E(J = {})'.format(J[j]))

        # Calcula os possíveis valores M do momento resultante
        M = operacoes.calcula_possiveis_m_iniciais(J[j])
        tam = len(M)

        # Em casos de soma de j's inteiro com semi-inteiro, também descontamos 1
        if type(j1) == sp.core.numbers.Half and type(j1) != type(j2):
            tam -= 1
        if type(j2) == sp.core.numbers.Half and type(j2) != type(j1):
            tam -= 1

        # Armazena todas as equações de um dado subespaço
        equacoes = []

        if j == 0:
            equacoes.append([[1, max(J), min(M)],
                            [[1, j1, j2, min(m1), min(m2)]]])
        else:
            equacoes.append(operacoes.muda_subespaco(conjunto, j1, j2, m1, m2))

            if conjunto[j-1][0][0][1] == 1:
                if latex:
                    display(Math(operacoes.printa_latex(equacoes[0])))
                else:
                    print(equacoes[0])
                conjunto.append(equacoes)
                break

        for i in range(tam):
            if latex:
                display(Math(operacoes.printa_latex(equacoes[i])))
            else:
                print(equacoes[i])
            equacoes.append(operacoes.j_mais(equacoes[i]))
        
        # Garante que a última equação não nula do subespaço seja impressa
        if equacoes[i][0][2]/equacoes[0][0][2] != -1:
            if latex:
                display(Math(operacoes.printa_latex(equacoes[i+1])))
            else:
                print(equacoes[i+1])
        
        print('')

        conjunto.append(equacoes)

        tam -= 2
        if tam<=0:
            tam = 1

    if aviso:
        print('Limite de subespaços atingido. \n')

