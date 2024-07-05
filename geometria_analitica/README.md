# Geometria Analítica 

## Aula 001 (Distância entre Pontos)
Distância entre Pontos

Se ambos coordenadas forem iguais, a distância é 0.
Ex: A(3,5) e B(3,5) como são iguais, a distância é 0

Se uma das coordenadas forem iguais, basta fazer a diferença do maior e do menor do outro eixo.
Ex: A(5,2) e B(5,9) o X é igual, então basta fazer a diferença do Y, sendo 9-2 = 7
Ex 2: A(4,6) e B(8,6) o Y é igual, então basta fazer a diferença do X, sendo 8-4 = 4

Se não for nenhum dos casos, basta projetar a reta paralela no eixo e calcular por pitágoras.
Ex: A(5,3) e B (7,4), como X e Y são diferentes ao mesmo tempo, tem que fazer por pitágoras.

## Aula 002 (Ponto Médio)
Ponto Médio entre 2 pontos do mesmo eixo (Eixo X e/ou Y)

Basta utilizar a média aritmética entre os pontos do mesmo eixo.

## Aula 003 (Baricentro ou Centro de Gravidade)
Baricentro de um triângulo, também conhecido como centro de gravidade, é o ponto central do triângulo.

Basta utilizar a média aritmética (nesse caso, são de 3 pontos) entre os pontos.

Baricentro é o encontro das retas das medianas dos 3 pontos do triângulo
A Mediana divide o outro lado igual em partes, exemplo: se um lado tem total de 8, ao dividir por uma mediana, fica 4 em cada lado.
E dividindo todos os lados com mediana, o encontro no centro desse triângulo é o baricentro

## Aula 004 (Alinhamento entre Pontos)
Alinhamento de 3 Pontos.

Basta ver a inclinação da reta (coeficiente angular) se são iguais
Se você tem 3 pontos (A, B, C) os 3 coeficiente angulares de AB deve ser igual ao coeficiente angular de BC

Para saber se 3 pontos estão alinhados (numa mesma reta), basta colocar ela numa matriz, completar a última coluna com 1 e calcular o determinante desta matriz, sendo = 0, estão alinhados.

Outro jeito de ver se os pontos estão alinhados, é com matriz
Basta colocar ela numa matriz, completar a última coluna com 1 e calcular o determinante desta matriz
Se o determinado for igual a 0, estão alinhados.

## Aula 005 (Equação Reduzida da Reta)
Equação Reduzida de uma Reta (Função do Primeiro Grau)

Como já consta no título, a equação reduzida da reta é uma função afim (do primeiro grau)

E o coeficiente angular (declividade da reta) é igual a tangente do ângulo.

```
Tangente = Cateto Oposto / Cateto Adjacente
```

## Aula 006 (Equação Geral da Reta)
A Equação Geral de uma reta é a Equação Fundamental só que simplificada.

### Equação Fundamental
```
y - ya = m (x - xa)
```

### Equação Geral
```
ax + by + c = 0
```

## Aula 007 (Paralelismo)
As retas serão paralelas se possuírem a mesma declividade (mesmo coeficiente angular) e se elas tiverem o mesmo coeficiente linear, é a mesma reta.
Exemplo: 2x + 5 e 2x + 8 são parelelas, mas são retas diferentes (por causa do coeficiente linear)
Exemplo 2: 4x + 5 e 4x + 5 são parelelas, e é a mesma reta (por causa do coeficiente linear)

## Aula 008 (Perpendicularismo)
As retas serão perpendiculares se o coeficiente angular foi o oposto da outra com sinal trocado.

### Primeira Reta 
```
2x + 5 
```
### Segunda Reta
```
1/2x + 8 
```

A primeira e a segunda reta são perpendiculares, pois o coeficiente angular da primeira é 2 e da segunda reta é -1/2

### Fórmulas 1
```
m1 = -1/m2
```

### Fórmula 2 (manipulando a equação da fórmula 1)
```
m1 * m2 = -1
```

## Aula 009 (Ângulo entre 2 Retas)

## Aula 010 (Distância da Reta para o Ponto)

## Aula 011 (Área do Triângulo)
Você conhecendo a coordenada dos 3 vértices do triângulo, basta jogar a coordenada na matriz 3x3 e calcular o determinante, fazer o módulo do determinante e dividir por 2, será a área do triângulo.

```
Área = (|Determinante|) / 2
```

## Aula 012 (Área do Quadrilátero)
O jeito mais simples é você traçar uma linha na diagonal do quadrilátero e ele será dividido em 2 partes, sendo 2 triângulos, então basta somar o determinante dos 2 triângulos e dividr por 2.

```
Área = (|Determinante do Primeiro Triângulo| + |Determinante do Segundo Triângulo|) / 2
```

## Aula 013 (Equação Reduzida da Circunferência)
A fórmula é bem parecida com a distância entre dois pontos.

```
(x - x0)² + (y - y0)² = R²
```

```
(x,y) é a coordenada de um ponto qualquer
```

```
(x0,y0) é a coordenada do centro da circunferência
```

```
R é o raio
```

## Aula 014 (Posição Relativa entre Ponto e a Circunferência)

Distância maior que raio --> Ponto está fora da circunferência (Externo)
Distância igual ao raio --> Ponto está em cima da linha da circunferência (Pertencente)
Distância menor ao raio --> Ponto está dentro da circunferência

Também é possível jogar as coordenadas dos pontos na equação reduzida da circunferência e resolver a equação

Resultado Maior que 0 --> Ponto está fora da circunferência (Externo)
Resultado Igual a 0  --> Ponto está em cima da linha da circunferência (Pertencente)
Resultado Menor que 0  --> Ponto está dentro da circunferência