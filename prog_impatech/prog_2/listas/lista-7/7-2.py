import heapq

# Classe para representar um grafo\class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.graph = []  # Lista de arestas

    # Adicionar uma aresta ao grafo
    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))

    # Função para encontrar a MST usando o algoritmo de Kruskal
    def find_mst(self):
        # Ordenar as arestas pelo peso
        self.graph.sort()
        parent = list(range(self.V))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x

        mst = []
        for weight, u, v in self.graph:
            if find(u) != find(v):
                mst.append((u, v, weight))
                union(u, v)
                if len(mst) == self.V - 1:
                    break

        return mst

# Exemplo de uso
g = Graph(5)
g.add_edge(0, 1, 1.0)
g.add_edge(0, 3, 2.0)
g.add_edge(1, 2, 3.0)
g.add_edge(1, 3, 1.5)
g.add_edge(2, 3, 2.5)
g.add_edge(3, 4, 1.2)

mst = g.find_mst()

# Imprimir as arestas da MST
for u, v, weight in mst:
    print(f"Aresta ({u}, {v}) com peso {weight:.2f}")

#para ordenação por si só o custo de implementação já é nlogn.

#o custo de implementacao deste codigo no pior caso (grafo denso) é n*2logn, então não é ótima.
