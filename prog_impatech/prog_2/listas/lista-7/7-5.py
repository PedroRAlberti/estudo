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
