#questão 1)

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


#questão 2)

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


#questão 3)

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# letra a)
def aproximacao1(data_x, data_y):
    def objetivo(params):
        a, b = params
        return np.sum(np.abs(a * data_x + b - data_y))

    inicial = [0, 0]

    resultado = minimize(objetivo, inicial, method='Powell')
    return resultado.x  

#letra b)

def generate_points(m):
    np.random.seed(1)
    a = 6
    b = -3
    x = np.linspace(0, 10, m)
    y = a * x + b + np.random.standard_cauchy(size=m) 
    return x, y

tamanhos = [64, 128, 256, 512, 1024]
resultados_aproximacao1 = []

for tamanho in tamanhos:
    data_x, data_y = generate_points(tamanho) 
    a, b = aproximacao1(data_x,data_y)    
    resultados_aproximacao1.append((a, b))
    print(f"Tamanho: {tamanho} -> Coeficientes ajustados: a = {a:.3f}, b = {b:.3f}")

#letra c)

def aproximacao2(data_x,data_y):
    x = np.array(data_x)
    y = np.array(data_y)

    sum_xi = np.sum(x)
    sum_yi = np.sum(y)
    sum_xi2 = np.sum(x**2)
    sum_xiyi = np.dot(x, y)
    k = len(x)  

    A = np.array([[sum_xi2, sum_xi], [sum_xi, k]])
    b = np.array([sum_xiyi, sum_yi])

    coef = np.linalg.solve(A, b)

    print(f'a reta pela aproximação2 é = {coef[0]:.3f}*x + {coef[1]:.3}.')
    return coef[0], coef[1]

#letra D)

def visualizar_ajustes(x, y, coef_L1, coef_L2):

    plt.figure(figsize=(10, 6))

    plt.scatter(x, y, label='Pontos (com ruído)', color='black', alpha=0.6)


    y_L1 = coef_L1[0] * x + coef_L1[1]
    plt.plot(x, y_L1, label=f'Ajuste L1: y = {coef_L1[0]:.4f}x + {coef_L1[1]:.4f}', color='blue')

    y_L2 = coef_L2[0] * x + coef_L2[1]
    plt.plot(x, y_L2, label=f'Ajuste L2: y = {coef_L2[0]:.4f}x + {coef_L2[1]:.4f}', color='red')

    plt.title('Comparação dos Ajustes L1 e L2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    x, y = generate_points(128)  

    coef_L1 = aproximacao1(x, y)  
    coef_L2 = aproximacao2(x, y)  

    visualizar_ajustes(x, y, coef_L1, coef_L2)

#letra e)

# para a aproximação 1 ) por todos os erros terem o mesmo peso, ele lida melhor dados que desviam muito do padrão.

# para a aproximação 2 ) pelo quadrado na sua formula possibilita o uso de derivar que torna computacionalmente mais eficiente para grandes massas de dados.