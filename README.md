# Mátematica IV
Algoritmos utilizados en matemática IV

# Método de Bisección

El método de bisección es un método numérico para encontrar raíces de funciones continuas. Este método se basa en el teorema del valor intermedio de las funciones continuas, que dice que cualquier función continua f (x) en el intervalo [a,b] que satisfaga f (a) * f (b) < 0 debe tener un cero en el intervalo [a,b].

## Algoritmo

El método de la bisección es un método simple y convergente para calcular la raíz de una función. Consiste en calcular el punto medio c=(a+b)/2 del intervalo [a, b] y sustituirlo por el intervalo [c, b] ó [a, c] dependiendo de cual contiene a la raíz r.

## Fórmulas

- Punto medio: $c = \frac{a + b}{2}$

- Error absoluto: $Ea = |(Xr - Xr_{ant})|$

- Error relativo: $Er = |\frac{(Xr - Xr_{ant})}{Xr}|$

- Criterio de parada: $Ea < Es$ o $Er < Ermax$

Donde:

- $Xr$: aproximación actual a la raíz.
- $Xr_{ant}$:: aproximación anterior a la raíz.
- $Es$: error absoluto máximo permitido.
- $Ermax$: error relativo máximo permitido.
