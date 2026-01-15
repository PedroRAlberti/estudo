#questao 1)
def find_nb(data, point):
    Dt = data - point
    d = np.linalg.norm(Dt, axis=1)
    idt = np.argmin(d)
    return d[idt], idt

#inicialmente é importante saber que o data é um array com uma lista de pontos, e o ponto é um ponto
#a função deste código é: dentre os pontos no data, qual é o mais próximo do point dado?
#agora ele faz um array com os pontos do data diminuídos do point, chamado Dt
#na linha 4 ele acha a norma de cada ponto em Dt, que na prática, é a distancia em módulo de cada ponto do data ao point
#nas linhas 5 e 6, respectivamente, ele pega o valor mínimo em d que é a menor distancia de algum ponto ao point e o retorna.
#como todos os passos são lineares, ou seja, O(n), temos que o programa é também O(n)

#questão 2 e 3)

import random

def generate_maze_iterative(m, n, room=0, wall=1, cheese='*'):
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]
    stack = [(0, 0)]  # Começa no canto superior esquerdo
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # N, S, W, E

    while stack:
        x, y = stack[-1]
        maze[2 * x + 1][2 * y + 1] = room  # Marca o caminho

        # Obtém as direções válidas
        valid_directions = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                valid_directions.append((dx, dy))

        if valid_directions:
            # Escolhe uma direção aleatória
            dx, dy = random.choice(valid_directions)
            maze[2 * x + 1 + dx][2 * y + 1 + dy] = room  # Abre a parede
            stack.append((x + dx, y + dy))  # Move para a nova posição
        else:
            stack.pop()  # Retorna se não houver direções válidas

    # Coloca o queijo em um local aleatório
    while True:
        i = random.randint(1, m * 2 - 1)
        j = random.randint(1, n * 2 - 1)
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze

def caminho_ate_o_queijo(maze):
    m = len(maze)
    n = len(maze[0])
    path = []
    visitados = []
    direcoes = [(1,0),(-1,0),(0,1),(0,-1)]
    def dps(coordenada):
        x,y = coordenada
        path.append((x,y))
        visitados.append((x,y))

        if maze[x][y] == '*':
            print("Queijo encontrado!")
            return path
        
        valid_directions = []
        for dx,dy in direcoes:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != 1 and ((nx,ny) not in visitados):
                valid_directions.append((dx,dy))

        while valid_directions:
            dx,dy = valid_directions.pop()
            res = dps((x + dx, y + dy))
            if res is not None:
                return res 

        if valid_directions == []:
            path.pop()
    
        return None
          
    return dps((1,1))           
    

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))            

if __name__ == '__main__':
    m, n = 5, 7  # Tamanho da grade
    random.seed(10110)
    maze = generate_maze_iterative(m, n)
    print("Labirinto gerado:")
    print_maze(maze)
    print(caminho_ate_o_queijo(maze))
    
# questão 4)

class Vertex:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class Graph:
    def __init__(self):
        self.dict = {}  # Dicionário para armazenar as adjacências
        self.dict_valores = {}  # Dicionário para armazenar os valores dos vértices

    def adjacent(self, x, y):
        """Verifica se o vértice y é adjacente ao vértice x."""
        if x.nome in self.dict and y.nome in self.dict:
            return y.nome in self.dict[x.nome]
        return False

    def add_vertex(self, x):
        """Adiciona o vértice x ao grafo. Retorna True se for adicionado, False se já existir."""
        if x.nome not in self.dict:
            self.dict[x.nome] = []  # Inicializa a lista de adjacência de x
            self.dict_valores[x.nome] = x.valor  # Armazena o valor de x
            return True
        return False

    def add_edge(self, x, y):
        """Adiciona uma aresta entre os vértices x e y. Retorna True se adicionada, False se já existir."""
        if x.nome in self.dict and y.nome in self.dict:
            if y.nome not in self.dict[x.nome]:
                self.dict[x.nome].append(y.nome)  # Adiciona y à lista de adjacência de x
                self.dict[y.nome].append(x.nome)  # Adiciona x à lista de adjacência de y (grafo não-direcionado)
                return True
            return False
        return False  # Pelo menos um dos vértices não existe

    def remove_edge(self, x, y):
        """Remove a aresta entre x e y. Retorna True se removida, False se não existir."""
        if x.nome in self.dict and y.nome in self.dict:
            if y.nome in self.dict[x.nome]:
                self.dict[x.nome].remove(y.nome)  # Remove y da lista de adjacência de x
                self.dict[y.nome].remove(x.nome)  # Remove x da lista de adjacência de y
                return True
        return False  # Aresta não existe

    def remove_vertex(self, x):
        """Remove o vértice x e todas as suas conexões. Retorna True se removido, False se não existir."""
        if x.nome in self.dict:
            # Remove o vértice x da lista de adjacências de todos os outros vértices
            for other in self.dict:
                if x.nome in self.dict[other]:
                    self.dict[other].remove(x.nome)

            # Remove o próprio vértice e seu valor
            del self.dict[x.nome]
            del self.dict_valores[x.nome]
            return True
        return False

    def get_neighbors(self, x):
        """Retorna a lista de vizinhos do vértice x."""
        if x.nome in self.dict:
            return self.dict[x.nome]
        return []
    
    def get_vertex_value(self, x):
        """Retorna o valor do vértice x."""
        if x.nome in self.dict_valores:
            return self.dict_valores[x.nome]
        return None
    
    def set_vertex_value(self, x, v):
        """Define um novo valor para o vértice x."""
        if x.nome in self.dict_valores:
            self.dict_valores[x.nome] = v
            return True
        return False

# Exemplo de uso e teste de cada função
if __name__ == "__main__":
    # Criando os vértices
    A = Vertex("A", 0)
    B = Vertex("B", 2)
    C = Vertex("C", 3)
    D = Vertex("D", 4)

    # Criando o grafo
    G = Graph()

    # Testando a função add_vertex
    print("Adicionando vértices:")
    print(G.add_vertex(A))  # True (A adicionado)
    print(G.add_vertex(B))  # True (B adicionado)
    print(G.add_vertex(C))  # True (C adicionado)
    print(G.add_vertex(D))  # True (D adicionado)
    print(G.add_vertex(A))  # False (A já existe)

    # Testando a função add_edge
    print("\nAdicionando arestas:")
    print(G.add_edge(A, B))  # True (Aresta A-B adicionada)
    print(G.add_edge(B, C))  # True (Aresta B-C adicionada)
    print(G.add_edge(A, C))  # True (Aresta A-C adicionada)
    print(G.add_edge(A, B))  # False (Aresta A-B já existe)

    # Testando a função adjacent
    print("\nVerificando adjacências:")
    print(G.adjacent(A, B))  # True
    print(G.adjacent(A, D))  # False
    print(G.adjacent(B, C))  # True

    # Testando a função get_neighbors
    print("\nVizinhos de A:", G.get_neighbors(A))  # ['B', 'C']
    print("Vizinhos de B:", G.get_neighbors(B))  # ['A', 'C']
    print("Vizinhos de D:", G.get_neighbors(D))  # []

    # Testando a função remove_edge
    print("\nRemovendo arestas:")
    print(G.remove_edge(A, B))  # True (Aresta A-B removida)
    print(G.remove_edge(A, B))  # False (Aresta A-B não existe mais)

    # Testando a função remove_vertex
    print("\nRemovendo vértices:")
    print(G.remove_vertex(A))  # True (Vértice A removido)
    print(G.remove_vertex(A))  # False (Vértice A já foi removido)

    # Verificando o estado do grafo
    print("\nEstado do grafo após remoções:")
    print("Dicionário de adjacências:", G.dict)
    print("Dicionário de valores:", G.dict_valores)

    # Testando a função get_vertex_value e set_vertex_value
    print("\nValores dos vértices:")
    print(f"Valor de B: {G.get_vertex_value(B)}")  # Valor original de B (2)
    print(f"Valor de C: {G.get_vertex_value(C)}")  # Valor original de C (3)

    # Testando a função set_vertex_value
    print("\nAlterando valores dos vértices:")
    G.set_vertex_value(B, 10)  # Alterando o valor de B para 10
    G.set_vertex_value(C, 5)   # Alterando o valor de C para 5
    print(f"Novo valor de B: {G.get_vertex_value(B)}")  # Novo valor de B (10)
    print(f"Novo valor de C: {G.get_vertex_value(C)}")  # Novo valor de C (5)")
