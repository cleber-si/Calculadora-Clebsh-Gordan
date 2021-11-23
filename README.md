# Calculadora dos Coeficientes de Clebsh-Gordan

**Autor:** [@cleber-si](https://github.com/cleber-si)

**Nota:** Projeto ainda em desenvolvimento e não estável! Ver lista dos principais problemas abaixo.

----

## Introdução

Os coeficientes de Clecsh-Gordan aparecem quando vamos fazer a soma de momenta (palavra que usarei para o plural de "momento angular") na mecânica quântica.

Considere um sistema arbitrário , cujo estado de fase seja &epsilon;, e um momento angular **J** relativo a esse sistema.

[...] 	Explicação breve da teoria de soma de momenta. (Colocarei em breve, prometo!)	 [...]

## Funcionamento

A representação das equações envolvendo os kets no código seguem o padrão:
$$
Equação & & Representação\ no\ Código\ (como\ array)\\ \\
\hline
\\

|2,2\rangle = |1, 1 ; 1, 1 \rangle & \Rightarrow& [[1, 2, 2], [[1, 1, 1, 1, 1]]] \\

|2, 1\rangle = \frac{1}{\sqrt{2}}[|1, 1 ; 1, 0 \rangle + |1, 1 ; 0, 1 \rangle] & \Rightarrow&
[[1, 2, 1], [[sqrt(2)/2, 1, 1, 1, 0], [sqrt(2)/2, 1, 1, 0, 1]]] \\

|1, -1\rangle = \frac{1}{\sqrt{2}}[|1, 1 ; 0, -1 \rangle - |1, 1 ; -1, 0 \rangle] & \Rightarrow&
[[1, 1, -1], [[sqrt(2)/2, 1, 1, 0, -1], [-sqrt(2)/2, 1, 1, -1, 0]]] \\

|J, M\rangle = \alpha |j_1, j_2 ; m_1, m_1 \rangle + \beta |j_1, j_2 ; m_1, m_1 \rangle +\ ... & \Rightarrow&
[[1, J, M], [[\alpha, 1, 1, 0, -1], [\beta, 1, 1, -1, 0],\ ...]] \\
$$
Em palavras, cada equação é representada por um array de tamanho 2 (chamarei de array da equação). O primeiro elemento do array guarda as informações do ket do lado esquedo da equação. Para esse caso, apenas três posições são necessárias: o valor do coeficiente (que sempre vai ser 1, exeto nos cálculos até chegar nesse resultado), o valor de **J** e o valor de **M**, respectivamente. Na segunda posição do array da equação, há um array de tamanho variado (pois o ket do lado esquerdo pode se dar como uma combinação linear de mais de um ket). Cada elemento desse array representa um ket seguindo o padrão: coeficiente (o de *Clebsh-Gordan*), **j1**, **j2**, **m1** e **m2**.

A ideia do código é que você simplesmente entre com os valores de  **j1** e **j2** e já veja todas as equações geradas por essa combinação de partículas, com os seus respectivos coeficientes.

## Principais Problemas (já sendo corrigidos)

* O código ainda não está bem organizado nem completamente comentado.
* Na troca de subespaços temos que resolver um sistema de equações. Essa implemetação só foi feita nos casos em que nos deparamos com um sistema de duas equações e duas incógnitas. Logo,  por hora o programa retorna resultados errados ou incompletos em casos onde a troca de subespaços envolve um sistema de ordem maior que 2.
* O programa ainda não suporta a soma de momenta com pelo menos um dos **j** sendo semi-inteiro (um elétron com spin 1/2, por exemplo). Por hora, apenas é possível somar partículas com momento angular inteiro.

## Implementações Futuras (algumas já em andamento)

* Interface gráfica
* Opção de imprimir todos os coeficientes de *Clebsh-Gordan* de uma vez.
* Dados **J**, **M**, **j1**, **j2**, **m1** e **m2**, o programa retornará o coeficiente de *Clebsh-Gordan* específico para essa configuração.

----

## Considerações

Este é um projeto completamente voluntário, cujo único propósito é exercitar as habilidades com programação e os conhecimentos de mecânica quântica. Sinta-se à vontade para dar qualquer contribuição ou sujestão para este projeto.