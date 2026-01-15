# a ideia inicial é fazer uma recursão onde ele faz a busca dos conectacos e após achar alguém ele faz a busca nesse

class Graph:
    def __init__(self, n, is_undirected=True):

        self.n = n
        self.is_undirected = is_undirected

        # Cria a lista de adjacência
        self.adj = []
        for _ in range(n):
            self.adj.append([])

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if self.is_undirected:  # Se o grafo for não direcionado
            self.adj[v].append(u)  # Adicionamos a aresta de v para u

    def count_components(self):

        self.visited = [
            False
        ] * self.n  # Cria um vetor que indica se um vértice já foi visitado ou não

        qtdComponents = 0  # Guarda a quantidade de componentes do nosso grafo

        for i in range(self.n):
            if not self.visited[i]:
                self.dfs(i)  # Marca todos os vértices que estão na mesma componente o i-ésimo vértice
                qtdComponents += 1

        return qtdComponents

    def dfs(self, current):
        self.visited[current] = True

        for i in range(
            len(self.adj[current])
        ):  # Itera por todos os vizinhos de current
            neighbour = self.adj[current][i]

            if not self.visited[neighbour]:
                self.dfs(neighbour)


# Lê o número de vértices e o número de arestas respectivamente
n, m = map(int, input().split())
graph = Graph(n)

for i in range(m):
    # Lê a descrição de uma aresta
    u, v = map(int, input().split())

    graph.add_edge(u, v)

print(f"Número de componentes: {graph.count_components()}")

