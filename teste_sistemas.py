import sympy as sp
from sympy.solvers.solveset import linsolve

# Define os coeficientes do sistema da troca de base a seren determinados (equivalentes a c1 e c2)
a, b, c = sp.symbols('a, b, c')

# Cria a matriz que representa o sistema
M = sp.Matrix(((1, 2, 1, 0), (1, 0, -1, 0)))

# Cria o sistema com base na matriz M
system = A, x = M[:, :-1], M[:, -1]

# Resolve o sistema
r = linsolve(system, a, b, c)

#print(r.args[0][1])

s = sp.solve(r.args[0][0]**2+r.args[0][1]**2+r.args[0][2]**2-1, c)

coef = max(s)

print(coef)

