import numpy as np
import matplotlib.pyplot as plt

class AproximadorPolinomio:
    def __init__(self, grau):
        """
        Inicializa a classe com o grau do polinômio.
        """
        if grau < 0:
            raise ValueError("O grau do polinômio deve ser um número inteiro não negativo.")
        self.grau = grau
        self.coeficientes = None

    def ajustar(self, x, y):
        """
        Ajusta os coeficientes do polinômio aos dados fornecidos (x, y).
        """
        if len(x) != len(y):
            raise ValueError("Os vetores x e y devem ter o mesmo tamanho.")

        # Cria a matriz de design com os termos do polinômio
        A = np.vander(x, self.grau + 1, increasing=False)
        
        # Resolve o sistema linear para encontrar os coeficientes
        self.coeficientes = np.linalg.lstsq(A, y, rcond=None)[0]

    def avaliar(self, x):
        """
        Avalia o polinômio ajustado nos pontos x.
        """
        if self.coeficientes is None:
            raise ValueError("O polinômio ainda não foi ajustado aos dados.")
        return np.polyval(self.coeficientes, x)

    def plotar(self, x, y, pontos_ajuste=100):
        """
        Plota os dados originais e a curva ajustada.
        """
        if self.coeficientes is None:
            raise ValueError("O polinômio ainda não foi ajustado aos dados.")

        # Gera valores para o gráfico do polinômio ajustado
        x_ajuste = np.linspace(min(x), max(x), pontos_ajuste)
        y_ajuste = self.avaliar(x_ajuste)

        # Cria o gráfico
        plt.figure(figsize=(8, 6))
        plt.scatter(x, y, color="blue", label="Dados originais")
        plt.plot(x_ajuste, y_ajuste, color="red", label=f"Polinômio de grau {self.grau}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.title("Ajuste de polinômio")
        plt.grid(True)
        plt.show()

# Exemplo de uso
if __name__ == "__main__":
    # Dados de exemplo
    x = np.array([-2, -1, 0, 1, 2])
    y = np.array([4, 1, 0, 1, 4])

    # Inicializa o ajustador com um polinômio de grau 2
    aproximador = AproximadorPolinomio(grau=2)
    aproximador.ajustar(x, y)

    # Avalia o polinômio em novos pontos
    x_teste = np.linspace(-2, 2, 100)
    y_teste = aproximador.avaliar(x_teste)

    # Plota os resultados
    aproximador.plotar(x, y)


class AproximadorPolinomioAutomatico:
    def __init__(self, grau_maximo=10, criterio="mse"):
        """
        Inicializa a classe com o grau máximo do polinômio e o critério de seleção.
        """
        if grau_maximo < 1:
            raise ValueError("O grau máximo deve ser pelo menos 1.")
        self.grau_maximo = grau_maximo
        self.criterio = criterio
        self.grau_ideal = None
        self.coeficientes = None

    def ajustar_automaticamente(self, x, y):
        """
        Ajusta automaticamente o melhor grau do polinômio aos dados fornecidos (x, y).
        """
        melhores_coeficientes = None
        menor_erro = float("inf")
        grau_ideal = 0

        for grau in range(0, self.grau_maximo + 1):
            # Ajuste do polinômio
            A = np.vander(x, grau + 1, increasing=False)
            coeficientes = np.linalg.lstsq(A, y, rcond=None)[0]

            # Predição e cálculo do erro
            y_pred = np.dot(A, coeficientes)
            mse = np.mean((y - y_pred) ** 2)

            # Seleção do melhor grau
            if mse < menor_erro:
                menor_erro = mse
                grau_ideal = grau
                melhores_coeficientes = coeficientes

        self.grau_ideal = grau_ideal
        self.coeficientes = melhores_coeficientes

    def avaliar(self, x):
        """
        Avalia o polinômio ajustado nos pontos x.
        """
        if self.coeficientes is None:
            raise ValueError("O polinômio ainda não foi ajustado automaticamente.")
        return np.polyval(self.coeficientes, x)

    def plotar(self, x, y, pontos_ajuste=100):
        """
        Plota os dados originais e a curva ajustada.
        """
        if self.coeficientes is None:
            raise ValueError("O polinômio ainda não foi ajustado automaticamente.")

        # Gera valores para o gráfico do polinômio ajustado
        x_ajuste = np.linspace(min(x), max(x), pontos_ajuste)
        y_ajuste = self.avaliar(x_ajuste)

        # Cria o gráfico
        plt.figure(figsize=(8, 6))
        plt.scatter(x, y, color="blue", label="Dados originais")
        plt.plot(x_ajuste, y_ajuste, color="red", label=f"Polinômio de grau {self.grau_ideal}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.title(f"Ajuste de polinômio (grau ideal = {self.grau_ideal})")
        plt.grid(True)
        plt.show()


# Função para gerar dados de teste
def gerar_dados_exemplo(ruido=0.5, n_pontos=50):
    """
    Gera um conjunto de dados simulados com ruído.
    """
    np.random.seed(15)
    x = np.linspace(-5, 5, n_pontos)
    y = 2 - 0.5 * x + 0.05 * x ** 3  # Polinômio de grau 3
    y += np.random.normal(0, ruido, n_pontos)  # Adiciona ruído
    return x, y

# Teste da classe
if __name__ == "__main__":
    # Gera dados simulados
    x, y = gerar_dados_exemplo()

    # Inicializa o aproximador automático
    aproximador = AproximadorPolinomioAutomatico(grau_maximo=10)
    aproximador.ajustar_automaticamente(x, y)

    # Exibe o grau ideal e plota os resultados
    print(f"Grau ideal encontrado: {aproximador.grau_ideal}")
    aproximador.plotar(x, y)
