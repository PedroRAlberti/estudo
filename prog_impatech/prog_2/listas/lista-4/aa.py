import numpy as np
# import matplotlib.pyplot as plt
from scipy.stats import uniform, norm, t

def sortear_pontos(N, distrib_x='uniforme', distrib_y='uniforme'):
    if distrib_x == 'uniforme':
        x = uniform.rvs(loc=-1, scale=2, size=N)  # Uniforme em [-1, 1]
    elif distrib_x == 'normal':
        x = norm.rvs(loc=0, scale=0.5, size=N)    # Normal com μ=0 e σ=0.5
    elif distrib_x == 'student_t':
        x = t.rvs(df=5, loc=0, scale=0.5, size=N)  # Student's t com μ=0 e σ=0.5

    if distrib_y == 'uniforme':
        y = uniform.rvs(loc=-1, scale=2, size=N)  # Uniforme em [-1, 1]
    elif distrib_y == 'normal':
        y = norm.rvs(loc=0, scale=0.5, size=N)    # Normal com μ=0 e σ=0.5
    elif distrib_y == 'student_t':
        y = t.rvs(df=5, loc=0, scale=0.5, size=N)  # Student's t com μ=0 e σ=0.5

    # Retornar os pontos como um numpy.array
    return np.array([x, y]).T  # Transpõe para que cada linha seja um ponto (x, y)

# def plotar_pontos(pontos):
#     plt.figure(figsize=(8, 8))
#     plt.scatter(pontos[:, 0], pontos[:, 1], c='blue', marker='o')
#     plt.xlim(-3, 3)  # Ajustar limites para visualização
#     plt.ylim(-3, 3)
#     plt.axhline(0, color='black', linewidth=0.5, ls='--')
#     plt.axvline(0, color='black', linewidth=0.5, ls='--')
#     plt.grid()
#     plt.title('Pontos sorteados no plano (x, y)')
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.show()

# Exemplo de uso
N = 100  # Número de pontos a sortear
pontos = sortear_pontos(N, distrib_x='normal', distrib_y='uniforme')
plotar_pontos(pontos)