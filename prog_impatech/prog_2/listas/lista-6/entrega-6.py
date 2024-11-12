from collections import deque

# usando o grafo utilizado da questão 4 da lista 5.
#os ultimos 2 metodos sao respectivamente as questões 1 e 2 da lista 6
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
    #questão 1)
    def bfs(self , vertice : Vertex):
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
    #questão 2)
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

# Realizando a busca em largura a partir do vértice A
print("\nBusca em Largura (BFS) a partir do vértice A:")
grafo.bfs(v1)

print(grafo.achar_valor_bfs(3))

with open("prog-2/listas/lista6/test_map2.txt", 'r') as arquivo:
    matriz = [[str(int(char)) for char in linha.strip()] for linha in arquivo]

#questão 1)
def descobrir_ilhas(matriz):
    m = len(matriz)
    n = len(matriz[0])
    visitadas = []
    terras = []
    ilhas = 0

    for i in range(m):
        for j in range(n):
            if matriz[i][j] == "1":
                terras.append((i,j))
    
    def dfs(coord : tuple):
        visitadas.append(coord)
        x , y = coord
        direcoes = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
        for dx,dy in direcoes:
            nx , ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matriz[nx][ny] == "1" and ((nx,ny)) not in visitadas:
                dfs((nx,ny))
        
    for i in terras:
        if i not in visitadas:
            ilhas += 1 
            dfs(i)

    return ilhas

print(descobrir_ilhas(matriz))

def centroides(matriz):
    m = len(matriz)
    n = len(matriz[0])
    visitadas = set() 
    terras = []
    ilhas = 0
    ilha = {}

    # Encontrar todas as células de terra (representadas por "1")
    for i in range(m):
        for j in range(n):
            if matriz[i][j] == "1":
                terras.append((i, j))
    
    # Função DFS para explorar as ilhas
    def dfs(coord):
        x, y = coord
        visitadas.add(coord)
        ilha[ilhas].append((x, y))  # Adiciona a célula à ilha
        direcoes = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matriz[nx][ny] == "1" and (nx, ny) not in visitadas:
                dfs((nx, ny))
    
    # Explorar todas as células de terra
    for i in terras:
        if i not in visitadas:
            ilhas += 1  # Encontrou uma nova ilha
            ilha[ilhas] = []  # Inicia uma lista para armazenar as células dessa ilha
            dfs(i)  # Chama o DFS para explorar essa ilha

    # Inicializar variáveis para os centroides
    centroide_maior = (0, 0)
    centroide_menor = (0, 0)
    maior_ilha = None  # Usado para armazenar o índice da maior ilha
    menor_ilha = None  # Usado para armazenar o índice da menor ilha
    maior_area = -1  # Usado para comparar o tamanho das ilhas
    menor_area = float('inf')  # Usado para comparar o tamanho das ilhas

    # Encontrar as ilhas com maior e menor número de células
    for i in range(1, ilhas + 1):
        ilha_size = len(ilha[i])  # Número de células da ilha
        if ilha_size > maior_area:
            maior_area = ilha_size
            maior_ilha = i  # Atualiza o índice da maior ilha

        if ilha_size < menor_area:
            menor_area = ilha_size
            menor_ilha = i  # Atualiza o índice da menor ilha

    # Calcular o centroide da maior ilha
    soma_x, soma_y = 0, 0
    for x, y in ilha[maior_ilha]:
        soma_x += x 
        soma_y += y 
    centroide_maior = (soma_x / maior_area, soma_y / maior_area)

    # Calcular o centroide da menor ilha
    soma_x, soma_y = 0, 0
    for x, y in ilha[menor_ilha]:
        soma_x += x 
        soma_y += y 
    centroide_menor = (soma_x / menor_area, soma_y / menor_area)
    print(ilha[menor_ilha])
    print(ilha[maior_ilha])
    # Retornar os centroides
    return f"O centroide da maior ilha é {centroide_maior} e o da menor ilha é {centroide_menor}"

print(centroides(matriz))

#questão 5)
import sys
sys.setrecursionlimit(10000)

def descobrir_lagos(matriz):
    m = len(matriz)
    n = len(matriz[0])
    visitadas = []
    agua = []
    lagos = {}
    aux = 0

    # Adiciona todas as células de água (células com "0") à lista de agua
    for i in range(m):
        for j in range(n):
            if matriz[i][j] == "0":
                agua.append((i, j))

    # Função DFS para explorar o lago
    def dfs(coord: tuple):
        x, y = coord
        visitadas.append(coord)
        if x == m - 1 or y == n - 1 or x == 0 or y == 0:
            lagos[aux] = False  # Se o lago tocar a borda, não é um lago fechado
        direcoes = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Direções: baixo, direita, cima, esquerda
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            # Verifica se está dentro da matriz e se é água não visitada
            if 0 <= nx < m and 0 <= ny < n and matriz[nx][ny] == "0" and (nx, ny) not in visitadas:
                dfs((nx, ny))

    # Explora todos os corpos d'água
    for i in agua:
        if i not in visitadas:
            aux += 1  # Identifica um novo lago
            lagos[aux] = True  # Inicialmente, assume que o lago é fechado
            dfs(i)

    lago = 0
    # Conta quantos lagos são realmente fechados
    for i in range(1, aux + 1):
        if lagos[i]:
            lago += 1

    if lago == 0:
        print("não há lagos")
        return False
    print("há pelo menos um lago, ou mais especificamente : " , lago, "lagos")
    return True

print(descobrir_lagos(matriz))