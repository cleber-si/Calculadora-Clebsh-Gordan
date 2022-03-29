import sympy as sp

x, y = sp.symbols('x y')

gfg_exp = x**2 - 4
  
print("Before Integration : {}".format(gfg_exp))
  
# Use sympy.integrate() method
intr = sp.solve(gfg_exp, x)
  
print("After Integration : {}".format(intr))

'''
[[1, 2, -2], [[1, 1, 1, -1, -1]]]
[[1, 2, -1], [[sqrt(2)/2, 1, 1, 0, -1], [sqrt(2)/2, 1, 1, -1, 0]]]
[[1, 2, 0], [[sqrt(6)/6, 1, 1, 1, -1], [sqrt(6)/3, 1, 1, 0, 0], [sqrt(6)/6, 1, 1, -1, 1]]]
[[1, 2, 1], [[sqrt(2)/2, 1, 1, 1, 0], [sqrt(2)/2, 1, 1, 0, 1]]]
[[1, 2, 2], [[1, 1, 1, 1, 1]]] 

[[1, 1, -1], [[sqrt(2)/2, 1, 1, 0, -1], [-sqrt(2)/2, 1, 1, -1, 0]]]
[[1, 1, 0], [[sqrt(2)/2, 1, 1, 1, -1], [-sqrt(2)/2, 1, 1, -1, 1]]]
[[1, 1, 1], [[sqrt(2)/2, 1, 1, 1, 0], [-sqrt(2)/2, 1, 1, 0, 1]]] 

[[1, 0, 0], [[-sqrt(2)/2, 1, 1, 1, -1], [-sqrt(2)/2, 1, 1, -1, 1]]]
'''