import numpy as np
from scipy.optimize import minimize

# Código da função de ajuste por L1
def ajustar_reta_L1(x, y):
    """
    Ajusta os coeficientes a e b para minimizar a soma dos valores absolutos dos resíduos.
    """
    def objetivo(params):
        a, b = params
        return np.sum(np.abs(a * x + b - y))

    inicial = [0, 0]  # Chute inicial para a e b
    resultado = minimize(objetivo, inicial, method='Powell')
    return resultado.x  # Coeficientes ajustados

# Função fornecida para gerar os pontos
def generate_points(m):
    np.random.seed(1)
    a = 6
    b = -3
    x = np.linspace(0, 10, m)
    y = a * x + b + np.random.standard_cauchy(size=m)  # Ruído da distribuição de Cauchy
    return x, y

# Testando para diferentes tamanhos de conjuntos de pontos
tamanhos = [64, 128, 256, 512, 1024]
resultados_L1 = []

print("Ajuste de coeficientes usando L1 (mínimos valores absolutos):")
for tamanho in tamanhos:
    x, y = generate_points(tamanho)  # Gerar pontos
    a, b = ajustar_reta_L1(x, y)    # Ajustar a reta
    resultados_L1.append((a, b))
    print(f"Tamanho: {tamanho} -> Coeficientes ajustados: a = {a:.4f}, b = {b:.4f}")
