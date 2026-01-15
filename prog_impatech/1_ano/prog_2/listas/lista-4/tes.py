import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm, t
from scipy.spatial import ConvexHull

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

# Exemplo de uso
N = 100 # Número de pontos a sortear
pontos = sortear_pontos(N, distrib_x='student_t', distrib_y='student_t')

def calcular_fecho_convexo(pontos):
    # Calcular o fecho convexo
    hull = ConvexHull(pontos)
    
    # Obter os pontos que pertencem ao fecho convexo
    pontos_fecho = pontos[hull.vertices]
    
    return np.array(pontos_fecho)
print(calcular_fecho_convexo(pontos))
