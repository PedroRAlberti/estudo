from collections import deque

class Vertex:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __rep__(self):
        return self.nome

class Graph:
    def __init__(self):
        self.dict = {}  # Dicionário para armazenar as adjacências
        self.dict_valores = {}  # Dicionário para armazenar os valores dos vértices
        self.fila = deque()
        self.visitados = []
    
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
    
    def bfs(self , vertice ):
        self.fila = deque()
        self.visitados =[]
        self.fila.append(vertice.nome)
        self.visitados.append(vertice.nome)
        while len(self.fila) > 0:
            atual = self.fila.popleft()
            print(f"Visitando: {atual}")
            for vizinho in self.dict[atual]:
                if vizinho not in self.visitados:
                    self.visitados.append(vizinho)
                    self.fila.append(vizinho)  

    def achar_valor_bfs(self,valor):
        self.fila = deque()
        self.visitados =[]
        init = list(self.dict.keys())[0]
        self.fila.append(init)
        self.visitados.append(init)
        while len(self.fila) > 0:
            atual = self.fila.popleft()
            if self.dict_valores[atual] == valor:
                break
            for vizinho in self.dict[atual]:
                if vizinho not in self.visitados:
                    self.visitados.append(vizinho)
                    self.fila.append(vizinho)  
        return atual


# Criando os vértices
v1 = Vertex('A', 1)
v2 = Vertex('B', 2)
v3 = Vertex('C', 3)
v4 = Vertex('D', 4)
v5 = Vertex('E', 5)

# Criando o grafo
grafo = Graph()

# Adicionando os vértices
grafo.add_vertex(v1)
grafo.add_vertex(v2)
grafo.add_vertex(v3)
grafo.add_vertex(v4)
grafo.add_vertex(v5)

# Adicionando as arestas (conexões entre os vértices)
grafo.add_edge(v1, v2)  # A <-> B
grafo.add_edge(v1, v3)  # A <-> C
grafo.add_edge(v2, v4)  # B <-> D
grafo.add_edge(v3, v5)  # C <-> E

# Exibindo o grafo
print("Lista de adjacências do grafo:")
for vertice, vizinhos in grafo.dict.items():
    print(f"{vertice}: {vizinhos}")

# Realizando a busca em largura a partir do vértice A
print("\nBusca em Largura (BFS) a partir do vértice A:")
grafo.bfs(v1)

print(grafo.achar_valor_bfs(3))