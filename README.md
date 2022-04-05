# Calculadora dos Coeficientes de Clebsh-Gordan

**Autor:** [@cleber-si](https://github.com/cleber-si)

**Nota:** Projeto ainda em desenvolvimento e não estável! Ver lista dos principais problemas abaixo.

----

## Introdução

Os coeficientes de Clecsh-Gordan aparecem quando vamos fazer a soma de momenta (palavra que usarei para o plural de "momento angular") na mecânica quântica.

Considere um sistema arbitrário, cujo estado de fase seja &epsilon;, e um momento angular **J** relativo a esse sistema, em que **J = j1 + j2**. É sempre possível construir uma base padrão {|k, j, m>} composta  por autovetores comuns a **J**² e Jz:
$$
\bold{J}^2 |k, j, m\rangle = j(j+1)\hbar^2|k, j, m\rangle \\
J_z |k, j, m\rangle = m \hbar |k, j, m\rangle
$$
de tal forma que a ação de operadores J+ e J- obedeça a relação
$$
J_{\pm} |k, j, m\rangle = \hbar \sqrt{j(j+1) - m(m \pm 1)} |k, j, m\rangle
$$
Denotamos por &epsilon;(k, j) o espaço vetorial gerado pelo conjunto de bases padao que corresponde a valores fixos de k e j. Existem (2j+1) desses vetores e eles podem ser transformados em qualquer ordem por **J**², Jz, J+ e J-. O estado de espaço pode ser considerado como sendo uma soma direta de subespaços ortogonais &epsilon;(k, j).

Assumamos então que uma base padrão {|k1, j1, m1>} seja conhecida no estado de espaço  &epsilon;1, composta de autovetores de **j1**² e j1z, onde **J1** é o operador momento angular do substema 1:
$$
\bold{J_1}^2 |k_1, j_1, m_1\rangle = j_1(j_1+1)\hbar^2|k_1, j_1, m_1\rangle \\
J_{1z} |k_1, j_1, m_1\rangle = m_1 \hbar |k_1, j_1, m_1\rangle \\ 
J_{1\pm} |k_1, j_1, m_1\rangle = \hbar \sqrt{j_1(j_1+1) - m_1(m_1 \pm 1)} |k_1, j_1, m_1\rangle
$$
Façamos o mesmo para uma outra base {|k2, j2, m2>}:
$$
\bold{J_2}^2 |k_2, j_2, m_2\rangle = j_2(j_2+1)\hbar^2|k_2, j_2, m_2\rangle \\
J_{2z} |k_2, j_2, m_2\rangle = m_2 \hbar |k_2, j_2, m_2\rangle \\ 
J_{2\pm} |k_2, j_2, m_2\rangle = \hbar \sqrt{j_2(j_2+1) - m_2(m_2 \pm 1)} |k_2, j_2, m_2\rangle
$$

$$
\otimes
$$

[...] 	Explicação breve da teoria de soma de momenta em desenvolvimento!	 [...]

## Funcionamento

A representação das equações envolvendo os kets no código seguem o padrão (Clique se estiver vendo isto com um tema escuro. Há também o código em LaTeX comentado neste arquivo.):

<!--
$$
\mbox{Equação} & & \mbox{Representação no Código (como array)}\\ \\
\hline
\\

|2,2\rangle = |1, 1 ; 1, 1 \rangle & \Rightarrow& [[1, 2, 2], [[1, 1, 1, 1, 1]]] \\

|2, 1\rangle = \frac{1}{\sqrt{2}}[|1, 1 ; 1, 0 \rangle + |1, 1 ; 0, 1 \rangle] & \Rightarrow&
[[1, 2, 1], [[sqrt(2)/2, 1, 1, 1, 0], [sqrt(2)/2, 1, 1, 0, 1]]] \\

|1, -1\rangle = \frac{1}{\sqrt{2}}[|1, 1 ; 0, -1 \rangle - |1, 1 ; -1, 0 \rangle] & \Rightarrow&
[[1, 1, -1], [[sqrt(2)/2, 1, 1, 0, -1], [-sqrt(2)/2, 1, 1, -1, 0]]] \\

|J, M\rangle = \alpha |j_1, j_2 ; m_1, m_1 \rangle + \beta |j_1, j_2 ; m_1, m_1 \rangle +\ ... & \Rightarrow&
[[1, J, M], [[\alpha, j_1, j_2, m_1, m_1], [\beta, j_1, j_2, m_1, m_1],\ ...]] \\
$$
-->
<img src="https://latex.codecogs.com/svg.image?\hspace{2.35cm}&space;\mbox{Equacao}\&space;\hspace{5.35cm}&space;\mbox{Representacao&space;no&space;Codigo&space;(como&space;array)}\\&space;\\|2,2\rangle&space;=&space;|1,&space;1&space;;&space;1,&space;1&space;\rangle&space;\hspace{5.35cm}&space;\&space;\Rightarrow&space;[[1,&space;2,&space;2],&space;[[1,&space;1,&space;1,&space;1,&space;1]]]&space;\\|2,&space;1\rangle&space;=&space;\frac{1}{\sqrt{2}}[|1,&space;1&space;;&space;1,&space;0&space;\rangle&space;&plus;&space;|1,&space;1&space;;&space;0,&space;1&space;\rangle]&space;\hspace{2.48cm}&space;\&space;\Rightarrow&space;\&space;[[1,&space;2,&space;1],&space;[[sqrt(2)/2,&space;1,&space;1,&space;1,&space;0],&space;[sqrt(2)/2,&space;1,&space;1,&space;0,&space;1]]]&space;\\|1,&space;-1\rangle&space;=&space;\frac{1}{\sqrt{2}}[|1,&space;1&space;;&space;0,&space;-1&space;\rangle&space;-&space;|1,&space;1&space;;&space;-1,&space;0&space;\rangle]&space;\hspace{1.48cm}&space;\&space;\Rightarrow\&space;[[1,&space;1,&space;-1],&space;[[sqrt(2)/2,&space;1,&space;1,&space;0,&space;-1],&space;[-sqrt(2)/2,&space;1,&space;1,&space;-1,&space;0]]]&space;\\|J,&space;M\rangle&space;=&space;\alpha&space;|j_1,&space;j_2&space;;&space;m_1,&space;m_1&space;\rangle&space;&plus;&space;\beta&space;|j_1,&space;j_2&space;;&space;m_1,&space;m_1&space;\rangle&space;&plus;\&space;...&space;\&space;\Rightarrow&space;\&space;[[\alpha,&space;j_1,&space;j_2,&space;m_1,&space;m_1],&space;[\beta,&space;j_1,&space;j_2,&space;m_1,&space;m_1],\&space;...]]&space;\\&space;" title="\hspace{2.35cm} \mbox{Equacao}\ \hspace{5.35cm} \mbox{Representacao no Codigo (como array)}\\ \\|2,2\rangle = |1, 1 ; 1, 1 \rangle \hspace{5.35cm} \ \Rightarrow [[1, 2, 2], [[1, 1, 1, 1, 1]]] \\|2, 1\rangle = \frac{1}{\sqrt{2}}[|1, 1 ; 1, 0 \rangle + |1, 1 ; 0, 1 \rangle] \hspace{2.48cm} \ \Rightarrow \ [[1, 2, 1], [[sqrt(2)/2, 1, 1, 1, 0], [sqrt(2)/2, 1, 1, 0, 1]]] \\|1, -1\rangle = \frac{1}{\sqrt{2}}[|1, 1 ; 0, -1 \rangle - |1, 1 ; -1, 0 \rangle] \hspace{1.48cm} \ \Rightarrow\ [[1, 1, -1], [[sqrt(2)/2, 1, 1, 0, -1], [-sqrt(2)/2, 1, 1, -1, 0]]] \\|J, M\rangle = \alpha |j_1, j_2 ; m_1, m_1 \rangle + \beta |j_1, j_2 ; m_1, m_1 \rangle +\ ... \ \Rightarrow \ [[\alpha, j_1, j_2, m_1, m_1], [\beta, j_1, j_2, m_1, m_1],\ ...]] \\ " />

Em palavras, cada equação é representada por um array de tamanho 2 (chamarei de array da equação). O primeiro elemento do array guarda as informações do ket do lado esquedo da equação. Para esse caso, apenas três posições são necessárias: o valor do coeficiente (que sempre vai ser 1, exeto nos cálculos até chegar nesse resultado), o valor de **J** e o valor de **M**, respectivamente. Na segunda posição do array da equação, há um array de tamanho variado (pois o ket do lado esquerdo pode se dar como uma combinação linear de mais de um ket). Cada elemento desse array representa um ket seguindo o padrão: coeficiente (o de *Clebsh-Gordan*), **j1**, **j2**, **m1** e **m2**.

A ideia do código é que você simplesmente entre com os valores de  **j1** e **j2** e já veja todas as equações geradas por essa combinação de partículas, com os seus respectivos coeficientes.

## Limitações

Na troca de subespaços temos que resolver um sistema de equações, que dizem respeito às condições de ortogonalidade no estado procurado no novo subestado com estados de outros subespaços. O tamanho desse sistema está diretamente relacionado com a quantidade  **k** de possíveis valores que **J** pode assumir. O sistema terá **k** variáveis e **k-1** equações. Isso resulta em um grau de liberdade, mas a equação de normalização do estado resultante do novo subespaço elimina esse grau de liberdade e nos retorna um valor usado na construção dos coeficientes do Clebsh-Gordan.

O número máximo para o tamanho desse sistema é **k = 7**. Ou seja, o algoritmo só vai retornar soluções completas quando **J** puder assumir até sete valores distintos. Um exemplo disso é o caso **j1 = j2 = 3**, onde **J = 6, 5, 4, 3, 2, 1, 0**. No caso onde **J** possa assumir mais valores, o código irá retornar apenas todos os estados dos primeiros sete subespaços superiores. 

## Implementações Futuras (algumas já em andamento)

* Interface gráfica
* Opção de imprimir todos os coeficientes de *Clebsh-Gordan* de uma vez.
* Dados **J**, **M**, **j1**, **j2**, **m1** e **m2**, o programa retornará o coeficiente de *Clebsh-Gordan* específico para essa configuração.

----

## Considerações

Este é um projeto completamente voluntário, cujo único propósito é exercitar as habilidades com programação e os conhecimentos de mecânica quântica. Sinta-se à vontade para dar qualquer contribuição ou sujestão para este projeto.
