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