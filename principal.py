import guia

# Deixe como True para exibir as equações formatadas em LaTeX
# (só para notebooks como Jupyter, Visual Code, PyCharm, Google Colab, etc.).
# Deixe como False para rodar no terminal ou com mais rapidez.
latex = False

# Recebe os momentos individuais
'''
Os valores de j1 e j2 devem ser escritos como uma string.
Vale lembrar que os valores devem ser inteiros ou semi-inteiros (n/2, onde n é um inteiro qualquer).
''' 
j1, j2 = "1", "1"

guia.calcula(j1, j2, latex)