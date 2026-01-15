import numpy as np
class Polinomio:
    def __init__(self, data_x, data_y, d):
        n = len(data_x)
        
        # Criação da matriz de Vandermonde
        X = np.zeros((n, d + 1))
        for i in range(n):
            for j in range(d + 1):
                X[i, j] = data_x[i]**j
        
        #calculo para achar o polinomio
        Xt = X.T
        XtX = np.dot(Xt, X)
        inv = np.linalg.inv(XtX)
        inv_Xt = np.dot(inv, Xt)
        Y = np.array(data_y)  
        A = np.dot(inv_Xt, Y)
        self.polinomio = A

    def __str__(self):
        terms = []
        for i, coef in enumerate(self.polinomio):
            if i == 0:
                terms.append(f"{coef:.2f}")
            else:
                if coef >= 0:
                    terms.append(f"+ {coef:.2f}x^{i}")
                else:
                    terms.append(f"- {abs(coef):.2f}x^{i}")
        return " ".join(terms)

    def evaluate(self, x):
        result = 0
        for i, coef in enumerate(self.polinomio):
            result += coef * (x ** i)
        return result


# Dados de exemplo
data_x = np.array([0, 1, 2, 3, 4])
data_y = np.array([1, 2.2, 3, 3.8, 5])
grau = 2

# Ajuste do polinômio
poly = Polinomio(data_x, data_y, 9)
print("Polinômio ajustado:")
print(poly)

# Avaliação do polinômio em um ponto
x_eval = 2.5
print(f"\nAvaliação do polinômio em x = {x_eval}:")
print(poly.evaluate(x_eval))