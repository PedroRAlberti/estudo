import numpy as np

class Poly_Interpolation:
    def __init__(self, data_x, data_y, max_d): 
        self.data_x = data_x
        self.data_y = data_y
        self.max_d = max_d
        self.best_poly = self.find_best_poly()

    def interpoled_poly(self, d):
        n = len(self.data_x)
        X = np.zeros((n, d + 1))
        for i in range(n):
            for j in range(d + 1):
                X[i, j] = self.data_x[i]**j

        Xt = X.T
        XtX = np.dot(Xt, X)
        inv = np.linalg.inv(XtX)
        Xt_inv = np.dot(inv, Xt)
        Y = self.data_y.T
        coeficients = np.dot(Xt_inv, Y)

        return coeficients

    def find_best_poly(self):
        r2_list = []
        best_poly = None
        for d in range(0, self.max_d + 1):
            coeficients = self.interpoled_poly(d)
            y_pred = np.array([self.evaluate(coeficients, x) for x in self.data_x])
            RSS = np.sum((self.data_y - y_pred) ** 2)
            y_mean = np.mean(self.data_y)
            RST = np.sum((self.data_y - y_mean) ** 2)    
            R_squared = 1 - (RSS / RST)
            r2_list.append(R_squared)
        
        best_degree = r2_list.index(max(r2_list))
        best_poly = self.interpoled_poly(best_degree)
        
        return best_poly

    def evaluate(self, poly, value=0):
        result = 0
        for c in poly[::-1]:
            result = c + result * value
        return result

    def __str__(self):
        # Converte os coeficientes para string e os separa por vírgula
        return ', '.join(f"{coef:.2f}" for coef in self.best_poly)

# Exemplo de uso:
data_x = np.array([0, 1, 2, 3, 4])
data_y = np.array([1, 2.2, 3, 3.8, 5])
max_degree = 5

poly_interpolation = Poly_Interpolation(data_x, data_y, max_degree)
print("Coeficientes do polinômio ajustado:")
print(poly_interpolation)


import matplotlib.pyplot as plt

# Visualizando os dados e o polinômio ajustado
x_vals = np.linspace(min(data_x), max(data_x), 100)  # Ponto de avaliação para o polinômio ajustado
y_vals = np.array([poly_interpolation.evaluate(poly_interpolation.best_poly, x) for x in x_vals])

plt.scatter(data_x, data_y, color='blue', label='Dados')
plt.plot(x_vals, y_vals, color='green', label='Polinômio Ajustado')
plt.legend()
plt.show()
