# Calculadora dos Coeficientes de Clebsh-Gordan

**Autor:** [@cleber-si](https://github.com/cleber-si) 

----

## Introdução

Os coeficientes de Clecsh-Gordan aparecem quando vamos fazer a soma de momenta (palavra que usarei para o plural de "momento angular") na mecânica quântica.

Considere um sistema arbitrário, cujo estado de fase seja &epsilon;, e um momento angular **J** relativo a esse sistema, em que **J = j1 + j2**. É sempre possível construir uma base padrão {|k, j, m>} composta  por autovetores comuns a **J**² e Jz:

<!--
$$
\bold{J}^2 |k, j, m\rangle = j(j+1)\hbar^2|k, j, m\rangle \\
J_z |k, j, m\rangle = m \hbar |k, j, m\rangle
$$
-->

<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}\begin{matrix}\bold{J}^2&space;|k,&space;j,&space;m\rangle&space;=&space;j(j&plus;1)\hbar^2|k,&space;j,&space;m\rangle&space;\\J_z&space;|k,&space;j,&space;m\rangle&space;=&space;m&space;\hbar&space;|k,&space;j,&space;m\rangle&space;\\\end{matrix}"   title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}\begin{matrix}\bold{J}^2  |k, j, m\rangle = j(j+1)\hbar^2|k, j, m\rangle \\J_z |k, j, m\rangle = m  \hbar |k, j, m\rangle \\\end{matrix}" />

de tal forma que a ação de operadores J+ e J- obedeça a relação

<!--
$$
J_{\pm} |k, j, m\rangle = \hbar \sqrt{j(j+1) - m(m \pm 1)} |k, j, m\rangle
$$
-->

<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}J_{\pm}&space;|k,&space;j,&space;m\rangle&space;=&space;\hbar&space;\sqrt{j(j&plus;1)&space;-&space;m(m&space;\pm&space;1)}&space;|k,&space;j,&space;m\rangle"  title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}J_{\pm}  |k, j, m\rangle = \hbar \sqrt{j(j+1) - m(m \pm 1)} |k, j, m\rangle"  />

Denotamos por &epsilon;(k, j) o espaço vetorial gerado pelo conjunto de bases padao que corresponde a valores fixos de k e j. Existem (2j+1) desses vetores e eles podem ser transformados em qualquer ordem por **J**², Jz, J+ e J-. O estado de espaço pode ser considerado como sendo uma soma direta de subespaços ortogonais &epsilon;(k, j).

Assumamos então que uma base padrão {|k1, j1, m1>} seja conhecida no estado de espaço  &epsilon;1, composta de autovetores de **j1**² e j1z, onde **J1** é o operador momento angular do substema 1:

<!--
$$
\bold{J_1}^2 |k_1, j_1, m_1\rangle = j_1(j_1+1)\hbar^2|k_1, j_1, m_1\rangle \\
J_{1z} |k_1, j_1, m_1\rangle = m_1 \hbar |k_1, j_1, m_1\rangle \\ 
J_{1\pm} |k_1, j_1, m_1\rangle = \hbar \sqrt{j_1(j_1+1) - m_1(m_1 \pm 1)} |k_1, j_1, m_1\rangle
$$
-->

<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}\begin{matrix}\bold{J_1}^2&space;|k_1,&space;j_1,&space;m_1\rangle&space;=&space;j_1(j_1&plus;1)\hbar^2|k_1,&space;j_1,&space;m_1\rangle&space;\\J_{1z}&space;|k_1,&space;j_1,&space;m_1\rangle&space;=&space;m_1&space;\hbar&space;|k_1,&space;j_1,&space;m_1\rangle&space;\\J_{1\pm}&space;|k_1,&space;j_1,&space;m_1\rangle&space;=&space;\hbar&space;\sqrt{j_1(j_1&plus;1)&space;-&space;m_1(m_1&space;\pm&space;1)}&space;|k_1,&space;j_1,&space;m_1\rangle\end{matrix}"   title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}\begin{matrix}\bold{J_1}^2  |k_1, j_1, m_1\rangle = j_1(j_1+1)\hbar^2|k_1, j_1, m_1\rangle \\J_{1z}  |k_1, j_1, m_1\rangle = m_1 \hbar |k_1, j_1, m_1\rangle \\J_{1\pm}  |k_1, j_1, m_1\rangle = \hbar \sqrt{j_1(j_1+1) - m_1(m_1 \pm 1)} |k_1,  j_1, m_1\rangle\end{matrix}" />

Façamos o mesmo para uma outra base {|k2, j2, m2>}:

<!--
$$
\bold{J_2}^2 |k_2, j_2, m_2\rangle = j_2(j_2+1)\hbar^2|k_2, j_2, m_2\rangle \\
J_{2z} |k_2, j_2, m_2\rangle = m_2 \hbar |k_2, j_2, m_2\rangle \\ 
J_{2\pm} |k_2, j_2, m_2\rangle = \hbar \sqrt{j_2(j_2+1) - m_2(m_2 \pm 1)} |k_2, j_2, m_2\rangle
$$

-->

<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}\begin{matrix}\bold{J_2}^2&space;|k_2,&space;j_2,&space;m_2\rangle&space;=&space;j_2(j_2&plus;1)\hbar^2|k_2,&space;j_2,&space;m_2\rangle&space;\\J_{2z}&space;|k_2,&space;j_2,&space;m_2\rangle&space;=&space;m_2&space;\hbar&space;|k_2,&space;j_2,&space;m_2\rangle&space;\\J_{2\pm}&space;|k_2,&space;j_2,&space;m_2\rangle&space;=&space;\hbar&space;\sqrt{j_2(j_2&plus;1)&space;-&space;m_2(m_2&space;\pm&space;1)}&space;|k_2,&space;j_2,&space;m_2\rangle\end{matrix}"   title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}\begin{matrix}\bold{J_2}^2  |k_2, j_2, m_2\rangle = j_2(j_2+1)\hbar^2|k_2, j_2, m_2\rangle \\J_{2z}  |k_2, j_2, m_2\rangle = m_2 \hbar |k_2, j_2, m_2\rangle \\J_{2\pm}  |k_2, j_2, m_2\rangle = \hbar \sqrt{j_2(j_2+1) - m_2(m_2 \pm 1)} |k_2,  j_2, m_2\rangle\end{matrix}" />

O estado de espaço do sistema global, formada pelos dois subsistemas acima, é o produto tensorial de &epsilon;1 e &epsilon;2:

<!--
$$
\varepsilon(k_1, k_2; j_1, j_2) = \varepsilon_1(k_1; j_1) \otimes \varepsilon_2 (k_2; j_2)
$$
-->

<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}\varepsilon(k_1,&space;k_2;&space;j_1,&space;j_2)&space;=&space;\varepsilon_1(k_1;&space;j_1)&space;\otimes&space;\varepsilon_2&space;(k_2;&space;j_2)"   title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}\varepsilon(k_1,  k_2; j_1, j_2) = \varepsilon_1(k_1; j_1) \otimes \varepsilon_2 (k_2;  j_2)" />

Vamos denotar por |k1, k2; j1, j2; m1, m2> os vetores dessa nova base. Mas podemos simplificar a notação ao omitir os índices k1 e k2. Assim:

<!--
$$
|j_1, j_2; m_1, m_2\rangle = |j_1, m_1 \rangle \otimes |j_2, m_2 \rangle
$$

-->

<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}|j_1,&space;j_2;&space;m_1,&space;m_2\rangle&space;=&space;|j_1,&space;m_1&space;\rangle&space;\otimes&space;|j_2,&space;m_2&space;\rangle"  title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}|j_1,  j_2; m_1, m_2\rangle = |j_1, m_1 \rangle \otimes |j_2, m_2 \rangle"  />

Vamos assimir agora que j1 e j2 sejam tais que j1 >= j2. Os vetores | j1, j2; m1, m2> já são autoestados de Jz:

<!--
$$
J_z |j_1, j_2; m_1, m_2\rangle & = & (J_{1z} + J_{2z}) |j_1, j_2; m_1, m_2\rangle \\
& = & (m_1 + m_2) \hbar |j_1, j_2; m_1, m_2\rangle
$$
-->

<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}\begin{matrix}J_z&space;|j_1,&space;j_2;&space;m_1,&space;m_2\rangle&space;&&space;=&space;&&space;(J_{1z}&space;&plus;&space;J_{2z})&space;|j_1,&space;j_2;&space;m_1,&space;m_2\rangle&space;\\&&space;=&space;&&space;(m_1&space;&plus;&space;m_2)&space;\hbar&space;|j_1,&space;j_2;&space;m_1,&space;m_2\rangle\end{matrix}"   title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}\begin{matrix}J_z  |j_1, j_2; m_1, m_2\rangle & = & (J_{1z} + J_{2z}) |j_1, j_2;  m_1, m_2\rangle \\& = & (m_1 + m_2) \hbar |j_1, j_2; m_1,  m_2\rangle\end{matrix}" />

e os autovalores correspondentes Mh (h-cortado) são tais que

<!--
$$
M = m_1 + m_2
$$
-->

<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}M&space;=&space;m_1&space;&plus;&space;m_2"  title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}M = m_1 +  m_2" />

Consequentemente, M pode assumir os valores

<!--
$$
j_1 + j_2, \ \ j_1+j_2-1, \ \ j_1+j_2-2, \ \ ..., \ \ -(j_1+j_2)
$$
-->

<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}j_1&space;&plus;&space;j_2,&space;\&space;\&space;j_1&plus;j_2-1,&space;\&space;\&space;j_1&plus;j_2-2,&space;\&space;\&space;...,&space;\&space;\&space;-(j_1&plus;j_2)"  title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}j_1 +  j_2, \ \ j_1+j_2-1, \ \ j_1+j_2-2, \ \ ..., \ \ -(j_1+j_2)" />

Além disso, os possíveis valores para J, dados j1 e j2, são:

<!--
$$
J = j_1 + j_2, \ j_1+j_2 - 1, \ j_1+j_2-2, \ ..., \ |j_1-j_2|
$$
-->

<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}J&space;=&space;j_1&space;&plus;&space;j_2,&space;\&space;j_1&plus;j_2&space;-&space;1,&space;\&space;j_1&plus;j_2-2,&space;\&space;...,&space;\&space;|j_1-j_2|"  title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}J = j_1 +  j_2, \ j_1+j_2 - 1, \ j_1+j_2-2, \ ..., \ |j_1-j_2|" />

Considerando que iniciemos as nossas análises no subespaço &epsilon;(J = j1 + j2), o primeiro autoestado que consideramos é tal que

<!--
$$
|J = j_1 + j_2, M = j_1 + j_2 \rangle = |j_1, j_2; m_1 = j_1, m_2 = j_2 \rangle
$$
-->

<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}|J&space;=&space;j_1&space;&plus;&space;j_2,&space;M&space;=&space;j_1&space;&plus;&space;j_2&space;\rangle&space;=&space;|j_1,&space;j_2;&space;m_1&space;=&space;j_1,&space;m_2&space;=&space;j_2&space;\rangle"  title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}|J = j_1  + j_2, M = j_1 + j_2 \rangle = |j_1, j_2; m_1 = j_1, m_2 = j_2 \rangle"  />

Podemos varrer todos os valores possíveis de M relativos ao subepaço considerado por meio dos operadores J_ ou J+, dados por

<!--
$$
J_{\pm}|J, \ M \rangle = \hbar \sqrt{J(J+1) - M(M\pm1)}
$$
-->

<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}J_{\pm}|J,&space;\&space;M&space;\rangle&space;=&space;\hbar&space;\sqrt{J(J&plus;1)&space;-&space;M(M\pm1)}"   title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}J_{\pm}|J,  \ M \rangle = \hbar \sqrt{J(J+1) - M(M\pm1)}" />

Se começarmos por |J=j1+j2, M=j1+j2>, usamos J_ para "descer" aos outros autoestados do subespaço.  Se começarmos por |J=j1+j2, M= - (j1+j2)>, usamos J+ para "subir" aos outros autoestados.

Após encontrar todos os possíveis autoestados de um subespaço, devemos trocar de subespaço. Por exemplo, de J = j1 + j2 para J = j1 + j2 - 1. Com isso, "varremos" todos os autoestados desse novo subespaço. Disso, trocamos mais uma vez de subespaço e fazemos a varredura mais uma vez e assim por diante até que todos os possíveis valores de J tenham sido explorados. Vale salientar que o processo de troca de subespaço leva em consideração um novo autoestado que deve ser perpendicular àqueles dos subespaços previamente trabalhados.

Para mais detalhes e formalismo acerca da teoria sobre momento angular e sobre a soma de momento angular em mecânica quântica, recomendo o estudo desses tópicos em livros como a coletânia [*Quantum Mechanics*](https://www.google.com.br/books/edition/Quantum_Mechanics_Volume_1/tVI_EAAAQBAJ?hl=pt-BR&gbpv=0) , de Cohen-Tannoudji, [*Modern Quantum Mechanics*](https://www.google.com.br/books/edition/Modern_Quantum_Mechanics/010yDwAAQBAJ?hl=pt-BR&gbpv=1&dq=sakurai&printsec=frontcover), de Sakurai & Napolitano, dentre outros.

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
<img  src="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}\begin{matrix}\mbox{Equa\c&space;c\~ao}&space;&&space;&&space;\mbox{Representa\c&space;c\~ao&space;no&space;C\'odigo&space;(como&space;array)}\\&space;\\\hline&space;\\|2,2\rangle&space;=&space;|1,&space;1&space;;&space;1,&space;1&space;\rangle&space;&&space;\Rightarrow&&space;[[1,&space;2,&space;2],&space;[[1,&space;1,&space;1,&space;1,&space;1]]]&space;\\|2,&space;1\rangle&space;=&space;\frac{1}{\sqrt{2}}[|1,&space;1&space;;&space;1,&space;0&space;\rangle&space;&plus;&space;|1,&space;1&space;;&space;0,&space;1&space;\rangle]&space;&&space;\Rightarrow&[[1,&space;2,&space;1],&space;[[sqrt(2)/2,&space;1,&space;1,&space;1,&space;0],&space;[sqrt(2)/2,&space;1,&space;1,&space;0,&space;1]]]&space;\\|1,&space;-1\rangle&space;=&space;\frac{1}{\sqrt{2}}[|1,&space;1&space;;&space;0,&space;-1&space;\rangle&space;-&space;|1,&space;1&space;;&space;-1,&space;0&space;\rangle]&space;&&space;\Rightarrow&[[1,&space;1,&space;-1],&space;[[sqrt(2)/2,&space;1,&space;1,&space;0,&space;-1],&space;[-sqrt(2)/2,&space;1,&space;1,&space;-1,&space;0]]]&space;\\|J,&space;M\rangle&space;=&space;\alpha&space;|j_1,&space;j_2&space;;&space;m_1,&space;m_1&space;\rangle&space;&plus;&space;\beta&space;|j_1,&space;j_2&space;;&space;m_1,&space;m_1&space;\rangle&space;&plus;\&space;...&space;&&space;\Rightarrow&[[1,&space;J,&space;M],&space;[[\alpha,&space;j_1,&space;j_2,&space;m_1,&space;m_1],&space;[\beta,&space;j_1,&space;j_2,&space;m_1,&space;m_1],\&space;...]]&space;\\\end{matrix}"   title="https://latex.codecogs.com/gif.image?\dpi{110}\bg{white}\begin{matrix}\mbox{Equa\c  c\~ao} & & \mbox{Representa\c c\~ao no C\'odigo (como array)}\\  \\\hline \\|2,2\rangle = |1, 1 ; 1, 1 \rangle & \Rightarrow&  [[1, 2, 2], [[1, 1, 1, 1, 1]]] \\|2, 1\rangle = \frac{1}{\sqrt{2}}[|1, 1  ; 1, 0 \rangle + |1, 1 ; 0, 1 \rangle] & \Rightarrow&[[1, 2,  1], [[sqrt(2)/2, 1, 1, 1, 0], [sqrt(2)/2, 1, 1, 0, 1]]] \\|1, -1\rangle =  \frac{1}{\sqrt{2}}[|1, 1 ; 0, -1 \rangle - |1, 1 ; -1, 0 \rangle] &  \Rightarrow&[[1, 1, -1], [[sqrt(2)/2, 1, 1, 0, -1], [-sqrt(2)/2, 1,  1, -1, 0]]] \\|J, M\rangle = \alpha |j_1, j_2 ; m_1, m_1 \rangle +  \beta |j_1, j_2 ; m_1, m_1 \rangle +\ ... & \Rightarrow&[[1, J,  M], [[\alpha, j_1, j_2, m_1, m_1], [\beta, j_1, j_2, m_1, m_1],\ ...]]  \\\end{matrix}" /> 

Em palavras, cada equação é representada por um array de tamanho 2 (chamarei de array da equação). O primeiro elemento do array guarda as informações do ket do lado esquedo da equação. Para esse caso, apenas três posições são necessárias: o valor do coeficiente (que sempre vai ser 1, exeto nos cálculos até chegar nesse resultado), o valor de **J** e o valor de **M**, respectivamente. Na segunda posição do array da equação, há um array de tamanho variado (pois o ket do lado esquerdo pode se dar como uma combinação linear de mais de um ket). Cada elemento desse array representa um ket seguindo o padrão: coeficiente (o de *Clebsh-Gordan*), **j1**, **j2**, **m1** e **m2**.

A ideia do código é que você simplesmente entre com os valores de  **j1** e **j2** no arquivo `principal.py` e já veja todas as equações geradas por essa combinação de partículas, com os seus respectivos coeficientes.

## Limitações

Na troca de subespaços temos que resolver um sistema de equações, que dizem respeito às condições de ortogonalidade no estado procurado no novo subestado com estados de outros subespaços. O tamanho desse sistema está diretamente relacionado com a quantidade  **k** de possíveis valores que **J** pode assumir. O sistema terá **k** variáveis e **k-1** equações. Isso resulta em um grau de liberdade, mas a equação de normalização do estado resultante do novo subespaço elimina esse grau de liberdade e nos retorna um valor usado na construção dos coeficientes do Clebsh-Gordan.

O número máximo para o tamanho desse sistema é **k = 7**. Ou seja, o algoritmo só vai retornar soluções completas quando **J** puder assumir até sete valores distintos. Um exemplo disso é o caso **j1 = j2 = 3**, onde **J = 6, 5, 4, 3, 2, 1, 0**. No caso onde **J** possa assumir mais valores, o código irá retornar apenas todos os estados dos primeiros sete subespaços superiores.

## Implementações Futuras (algumas já em andamento)

* Interface gráfica;
* Dados **J**, **M**, **j1**, **j2**, **m1** e **m2**, o programa retornará o coeficiente de *Clebsh-Gordan* específico para essa configuração.

----

## Considerações

Este é um projeto completamente voluntário, cujo único propósito é exercitar as habilidades com programação e os conhecimentos de mecânica quântica. Sinta-se à vontade para dar qualquer contribuição ou sujestão para este projeto.
