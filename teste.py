import sympy as sp
import operacoes

j1 = "3"

j1 = sp.parse_expr(j1)

# Calcula os m de cada partícula
# m1 = [i for i in range(-j1, j1+1)]

m1 = operacoes.calcula_possiveis_m(j1)

print(type(j1) ==  sp.core.numbers.Integer)
print(isinstance(j1, sp.core.numbers.Rational))
print(isinstance(j1, sp.core.numbers.Integer))