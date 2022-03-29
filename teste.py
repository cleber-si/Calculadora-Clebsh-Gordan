import sympy as sp
import operacoes

j1 = "1"
j2 = "1/2"

j1 = sp.parse_expr(j1)
j2 = sp.parse_expr(j2)

# Calcula os m de cada partícula
# m1 = [i for i in range(-j1, j1+1)]

m1 = operacoes.calcula_possiveis_m(j1)

#print(type(j1) ==  sp.core.numbers.Integer)
#print(isinstance(j1, sp.core.numbers.Rational))
#print(isinstance(j1, sp.core.numbers.Integer))
if type(j1) == sp.core.numbers.Half and type(j1) != type(j2):
    print('Inteiro e semi-inteiro')
if type(j2) == sp.core.numbers.Half and type(j1) != type(j2):
    print('Inteiro e semi-inteiro')