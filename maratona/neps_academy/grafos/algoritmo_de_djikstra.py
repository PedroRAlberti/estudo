import math
from queue import PriorityQueue


class Graph:
    def __init__(self, n, is_undirected=True):

        self.n = n
        self.is_undirected = is_undirected

        # Cria as listas de adjacências
        self.adj = []
        for _ in range(n):
            self.adj.append([])

    def add_edge(self, u, v, w):
        self.adj[u].append([v, w])
        if self.is_undirected:  # Se o grafo não for direcionado
            self.adj[v].append([u, w])  # Adicionamos a aresta de v para u

    def dijkstra(self, s):
        dist = [
            math.inf
        ] * self.n  # dist[i] = menor caminho entre s e i encontrado até agora
        mark = [False] * self.n
        # mark[i] = true, se e somente se, nós já tivermos achado o menor caminho entre s e i

        pq = PriorityQueue()

        dist[s] = 0
        pq.put([0, s])

        for k in range(self.n):

            while True:  # Acha o vértice desejado
                current = pq.get()[1]  # Pega o topo da nossa priority queue e remove-o

                if not mark[current]:  # Checa se o vértice atual não está marcado
                    break

            mark[current] = True

            for j in range(len(self.adj[current])):
                neighbour = self.adj[current][j][0]
                w = self.adj[current][j][1]

                if dist[neighbour] > dist[current] + w:
                    dist[neighbour] = dist[current] + w
                    pq.put([dist[neighbour], neighbour])

        return dist


# Lê o número de vértices, o número de arestas e a fonte
n, m, s = map(int, input().split())

graph = Graph(n)

for i in range(m):
    # Lê a descrição de uma aresta
    u, v, w = map(int, input().split())

    graph.add_edge(u, v, w)

dist = graph.dijkstra(s)

for i in range(n):
    print(f"A distância entre {s} e {i} é {dist[i]}")

