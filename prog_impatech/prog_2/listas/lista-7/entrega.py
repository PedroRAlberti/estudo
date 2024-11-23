#questao 1)
def find_judge(n, trust):
    # Inicializar uma matriz de confiança n x n
    trust_matrix = [[0] * (n + 1) for _ in range(n + 1)]

    # Preencher a matriz com as relações de confiança
    for a, b in trust:
        trust_matrix[a][b] = 1

    # Lista de possíveis candidatos a juiz
    possible_candidates = []

    # Verificar as linhas para ver quem é confiado por todos
    for person in range(1, n + 1):
        if all(trust_matrix[other][person] == 1 or other == person for other in range(1, n + 1)):
            possible_candidates.append(person)

    # Verificar se os candidatos não confiam em ninguém
    for candidate in possible_candidates:
        if all(trust_matrix[candidate][other] == 0 for other in range(1, n + 1)):
            return candidate

    # Se nenhum candidato satisfaz as condições, retornar -1
    return -1

# Exemplo de uso
t = [[1, 2], [2, 3], [1, 3]]
n = 3
print(find_judge(n, t))  # Saída esperada: 3
t = [[1, 3], [2, 3], [3, 1]]
print(find_judge(n, t))  # Saída esperada: -1

#questao 2)

import heapq

# Classe para representar um grafo\class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.graph = []  # Lista de arestas

    # Adicionar uma aresta ao grafo
    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))

    # Função para encontrar a MST usando o algoritmo de Kruskal
    def find_mst(self):
        # Ordenar as arestas pelo peso
        self.graph.sort()
        parent = list(range(self.V))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x

        mst = []
        for weight, u, v in self.graph:
            if find(u) != find(v):
                mst.append((u, v, weight))
                union(u, v)
                if len(mst) == self.V - 1:
                    break

        return mst

# Exemplo de uso
g = Graph(5)
g.add_edge(0, 1, 1.0)
g.add_edge(0, 3, 2.0)
g.add_edge(1, 2, 3.0)
g.add_edge(1, 3, 1.5)
g.add_edge(2, 3, 2.5)
g.add_edge(3, 4, 1.2)

mst = g.find_mst()

# Imprimir as arestas da MST
for u, v, weight in mst:
    print(f"Aresta ({u}, {v}) com peso {weight:.2f}")

#para ordenação por si só o custo de implementação já é nlogn.

#o custo de implementacao deste codigo no pior caso (grafo denso) é n*2logn, então não é ótima.


#questao 3)
import numpy as np
from scipy.interpolate import lagrange

# Dados fornecidos
altitudes = np.array([200, 400, 600, 800, 1000, 1200, 1400])
temperatures = np.array([15, 9, 5, 3, -2, -5, -15])

# Construir o polinômio de Lagrange
lagrange_poly = lagrange(altitudes, temperatures)

# Função para encontrar a altitude que corresponde a 0 graus Celsius usando método de busca por sinais opostos
def find_zero_temperature(poly, start, end, step=1):
    alt_range = np.arange(start, end, step)
    for i in range(len(alt_range) - 1):
        if poly(alt_range[i]) * poly(alt_range[i + 1]) < 0:  # Verificar mudança de sinal
            return (alt_range[i] + alt_range[i + 1]) / 2  # Retornar a média dos pontos
    return None

# Encontrar a altitude em que a temperatura é aproximadamente 0 graus
altitude_zero_temp = find_zero_temperature(lagrange_poly, 200, 1400)
if altitude_zero_temp:
    print(f"A altitude em que a temperatura é aproximadamente 0°C: {altitude_zero_temp:.2f} metros")
else:
    print("Nenhuma altitude com temperatura de 0°C encontrada no intervalo fornecido.")

# Estimar a temperatura a 700 metros
temperature_at_700 = lagrange_poly(700)
print(f"A temperatura estimada a 700 metros é: {temperature_at_700:.2f}°C")


# questao 4)

import numpy as np

class Interval:
    def __init__(self, p1, p2):
        self.inff, self.supp = min(p1, p2), max(p1, p2)
    
    @property
    def min(self):
        return self.inff

    @property
    def max(self):
        return self.supp
    
    @property
    def size(self):
        return (self.max - self.min)
    
    @property
    def haf(self):
        return (self.max + self.min) / 2.0
    
    def __contains__(self, x):
        return np.all(np.logical_and(self.inff <= x, x <= self.supp))

    def __str__(self):
        return f'[{self.inff:.4f}, {self.supp:.4f}]'

    def __repr__(self):
        return f'Interval({self.inff:.4f}, {self.supp:.4f})'

    def copy(self):
        return Interval(self.inff, self.supp)

# Classe para representar uma função real
class RealFunction:
    def __init__(self, func, derivative=None):
        self.func = func
        self.derivative = derivative

    def evaluate(self, x):
        return self.func(x)

    def evaluate_derivative(self, x):
        if self.derivative is not None:
            return self.derivative(x)
        raise ValueError("Derivative function not provided")

# Método de Newton para encontrar raízes
def newton_root(func, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        f_x = func.evaluate(x)
        f_prime_x = func.evaluate_derivative(x)
        if abs(f_x) < tol:
            return x
        if f_prime_x == 0:
            raise ValueError("Derivada zero. Método de Newton falhou.")
        x -= f_x / f_prime_x
    raise ValueError("Número máximo de iterações atingido")

# Método de busca por bisseção
def bissect(func, a, b, tol=1e-6, max_iter=100):
    if func.evaluate(a) * func.evaluate(b) >= 0:
        raise ValueError("A função deve ter sinais opostos em a e b")
    for _ in range(max_iter):
        c = (a + b) / 2
        f_c = func.evaluate(c)
        if abs(f_c) < tol or (b - a) / 2 < tol:
            return c
        if func.evaluate(a) * f_c < 0:
            b = c
        else:
            a = c
    raise ValueError("Número máximo de iterações atingido")

# Método de busca em grade
def grid_search(func, interval, step=0.01):
    if not isinstance(interval, Interval):
        raise ValueError("O parâmetro 'interval' deve ser uma instância da classe Interval")

    x = interval.min
    best_x = x
    min_value = abs(func.evaluate(x))
    while x <= interval.max:
        current_value = abs(func.evaluate(x))
        if current_value < min_value:
            min_value = current_value
            best_x = x
        x += step
    return best_x

# Exemplo de uso
def main():
    func = RealFunction(
        lambda x: x**3 - 2*x - 5,
        lambda x: 3*x**2 - 2
    )

    # Método de Newton
    x0 = 2  # Ponto inicial
    try:
        root_newton = newton_root(func, x0)
        print(f"Raiz encontrada pelo método de Newton: {root_newton:.6f}")
    except ValueError as e:
        print(f"Erro no método de Newton: {e}")

    # Método da bisseção
    try:
        root_bissect = bissect(func, 1, 3)
        print(f"Raiz encontrada pelo método da bisseção: {root_bissect:.6f}")
    except ValueError as e:
        print(f"Erro no método da bisseção: {e}")

    # Método de busca em grade
    interval = Interval(1, 3)
    try:
        root_grid = grid_search(func, interval, step=0.001)
        print(f"Raiz aproximada encontrada pela busca em grade: {root_grid:.6f}")
    except ValueError as e:
        print(f"Erro na busca em grade: {e}")

if __name__ == "__main__":
    main()

#questao 5)

import numpy as np
from scipy.interpolate import lagrange
import time

class interpolater:
    def evaluate(self, X):
        raise NotImplementedError

    def __call__(self, X):
        return self.evaluate(X)

class VandermondeMatrix(interpolater):
    def __init__(self, x, y):
        if len(x) != len(y):
            raise RuntimeError(f"Dimensions must be equal len(x) = {len(x)} != len(y) = {len(y)}")
        self.data = [x, y]
        self._degree = len(x) - 1
        self._buildMatrix()
        self._poly = np.linalg.solve(self.matrix, self.data[1])

    def _buildMatrix(self):
        self.matrix = np.ones([self._degree + 1, self._degree + 1])
        for i, x in enumerate(self.data[0]):
            self.matrix[i, 1:] = np.multiply.accumulate(np.repeat(x, self._degree))

    def evaluate(self, X):
        r = 0.0
        for c in self._poly[::-1]:
            r = c + r * X
        return r

# Nova classe para interpolação de Lagrange
class LagrangeInterpolator(interpolater):
    def __init__(self, x, y):
        if len(x) != len(y):
            raise RuntimeError(f"Dimensions must be equal len(x) = {len(x)} != len(y) = {len(y)}")
        self.poly = lagrange(x, y)

    def evaluate(self, X):
        return self.poly(X)

# Função para comparar o tempo de construção
def compare_construction_speed(x_points, y_points):
    start_time = time.time()
    vandermonde = VandermondeMatrix(x_points, y_points)
    time_vandermonde = time.time() - start_time

    start_time = time.time()
    lagrange_interp = LagrangeInterpolator(x_points, y_points)
    time_lagrange = time.time() - start_time

    print(f"Tempo de construção (Vandermonde): {time_vandermonde:.6f} segundos")
    print(f"Tempo de construção (Lagrange): {time_lagrange:.6f} segundos")

# Exemplo de uso
x_points = np.array([0, 1, 2, 3, 4])
y_points = np.array([1, 2, 0, 2, 1])

compare_construction_speed(x_points, y_points)
