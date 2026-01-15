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
