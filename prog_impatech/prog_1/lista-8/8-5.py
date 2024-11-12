import turtle

def desenhar_poligono(poligonos):
    # Inicializa a tela e a caneta (turtle)
    tela = turtle.Screen()
    caneta = turtle.Turtle()

    for i in poligonos:
        quantidade_de_pontos = len(poligonos[i][1])
        #este primeiro for é para desenhar cada poligono que está no objeto dado 
        # Define a cor da caneta
        caneta.color([i][1][-1])

        # Levanta a caneta para evitar desenhar linhas ao se movimentar
        caneta.penup()

        # Move para o primeiro vértice (ponto inicial)
        caneta.goto(poligonos[i][1][0])

        # Baixa a caneta para começar a desenhar
        caneta.pendown()

        # Desenha o polígono
        for j in range(quantidade_de_pontos):
            caneta.goto(poligonos[i][1][j])

        # Fecha o polígono
        caneta.goto(vertices[0])

    # Completa o desenho
    turtle.done()

# Exemplo de uso:
vertices = [(50, 50), (-50, 50), (-50, -50), (50, -50)]  # Lista de pontos (vértices) do polígono
cor = "blue"  # Cor do polígono
vertices2 = []

# desenhar_poligono(vertices, cor)
desenhar_poligono()
