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
