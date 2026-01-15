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
    stack = [(1,1)]
    path = []
    visitados = []
    direcoes = [(1,0),(-1,0),(0,1),(0,-1)]

    def dps(coordenada):
        x,y = coordenada
        path.append((x,y))
        visitados.append((x,y))
        print(path)

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
            dps((x + dx, y + dy))

        if valid_directions == []:
            path.pop()
    return(dps((1,1)))            
    

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