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
