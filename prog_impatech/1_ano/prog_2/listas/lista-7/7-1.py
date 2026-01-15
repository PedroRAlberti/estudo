def find_judge(n, trust):
    # Inicializar uma matriz de confiança n x n
    trust_matrix = [[0] * (n + 1) for _ in range(n + 1)]

    # Preencher a matriz com as relações de confiança
    for a, b in trust:
        trust_matrix[a][b] = 1

    # Lista de possíveis candidatos a juiz
    possible_candidates = []

    # Verificar as linhas para ver quem é confiado por todos
    for person in range(1, n + 1):
        if all(trust_matrix[other][person] == 1 or other == person for other in range(1, n + 1)):
            possible_candidates.append(person)

    # Verificar se os candidatos não confiam em ninguém
    for candidate in possible_candidates:
        if all(trust_matrix[candidate][other] == 0 for other in range(1, n + 1)):
            return candidate

    # Se nenhum candidato satisfaz as condições, retornar -1
    return -1

# Exemplo de uso
t = [[1, 2], [2, 3], [1, 3]]
n = 3
print(find_judge(n, t))  # Saída esperada: 3
t = [[1, 3], [2, 3], [3, 1]]
print(find_judge(n, t))  # Saída esperada: -1
