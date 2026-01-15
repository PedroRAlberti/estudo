#questão 1)
#primeiro vou copiar o codigo de arvore que o prof. emilio fez e colocou no github
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

# Function to create a BST from a list of nodes
def create_tree(nodes):
    if not nodes:  # Handle edge case when nodes list is empty
        return None
    
    root = TreeNode(nodes[0])
    
    def insert_node(root, value):
        current_node = root
        while current_node:
            if value < current_node.val:
                if current_node.left is None:
                    current_node.left = TreeNode(value)
                    break
                current_node = current_node.left
            elif value > current_node.val:
                if current_node.right is None:
                    current_node.right = TreeNode(value)
                    break
                current_node = current_node.right
            else:
                # Duplicate value found, return None to indicate an error
                print(f"Duplicate value {value} found. BST cannot have duplicate values.")
                return None
        return root

    for n in nodes[1:]:
        if insert_node(root, n) is None:
            return None  # Return None if a duplicate is found
    
    return root

# a ideia é comparar cada subarvore, e quando alguma subarvore for desbalanceada, todas as acima serão.
def check_height(node):
    if node is None:
        return 0
    
    left_height = check_height(node.left)
    if left_height == -1:  # Subárvore esquerda não é balanceada
        return -1
    
    right_height = check_height(node.right)
    if right_height == -1:  # Subárvore direita não é balanceada
        return -1
    
    if abs(left_height - right_height) > 1:  # Verifica o balanceamento
        return -1  # Árvore não é balanceada
    
    return max(left_height, right_height) + 1  # Retorna a altura da árvore

def is_balanced(root):
    return check_height(root) != -1

#criarei alguns testes de exemplo
ts1 = create_tree([128, 64, 256, 32, 96, 80, 112, 512, 384])
ts2 = create_tree([10, 5, 15, 3, 7, 12, 20])
ts3 = create_tree([10,9,8,7])

# Verificar se a árvore é balanceada
if is_balanced(ts1):
    print("A árvore {ts1} está balanceada.")
else:
    print("A árvore {ts1} não está balanceada.")

if is_balanced(ts2):
    print("A árvore {ts2} está balanceada.")
else:
    print("A árvore {ts2} não está balanceada.")

if is_balanced(ts3):
    print("A árvore {ts3} está balanceada.")
else:
    print("A árvore {ts3} não está balanceada.")

#questão 2)

import random
import time

class pilha():
    def __init__(self,lista):
        self.lista = lista
        self.tamanho = len(lista)

    def append(self,valor):
        self.lista.append(valor)
        self.tamanho += 1

    def pop(self):
        i = random.randint(0, self.tamanho - 1)
        self.lista[i] = self.lista[-1]
        self.lista.pop()
        self.tamanho -= 1 

    def __str__(self):
        return str(self.lista)

def test_pop_time(sizes):
    for size in sizes:
        # Criar uma instância de pilha com a lista de tamanho 'size'
        pilha_instance = pilha(list(range(size)))

        # Medir o tempo de execução do método pop
        start_time = time.time()
        pilha_instance.pop()  # Executa o pop
        end_time = time.time()

        print(f"Tamanho da pilha: {size}, Tempo para .pop(): {end_time - start_time:.10f} segundos")

# Exemplos de tamanhos variados
sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000,1_000_00000]
test_pop_time(sizes)

#questao 3)

#a) a ideia central seria ao criar a classe de nó ter a instancia valor do nó propriamente e uma lista tendo os nós filhos.
#b) ao adicionar um nó filho seria o análogo à dar append na lista de nós filhos de algum nó
#c) fazendo por profundidade: eu faria uma recursao na seguinte ideia:
# def busca(no):
#   if no.filho == none:
#       print no.val
#   for filho in no.filho:
#       busca(filho)

#questão 4)

import numpy as np
from scipy.stats import uniform, norm, t

def sortear_pontos(N, distrib_x='uniforme', distrib_y='uniforme'):
    if distrib_x == 'uniforme':
        x = uniform.rvs(loc=-1, scale=2, size=N)  # Uniforme em [-1, 1]
    elif distrib_x == 'normal':
        x = norm.rvs(loc=0, scale=0.5, size=N)    # Normal com μ=0 e σ=0.5
    elif distrib_x == 'student_t':
        x = t.rvs(df=5, loc=0, scale=0.5, size=N)  # Student's t com μ=0 e σ=0.5

    if distrib_y == 'uniforme':
        y = uniform.rvs(loc=-1, scale=2, size=N)  # Uniforme em [-1, 1]
    elif distrib_y == 'normal':
        y = norm.rvs(loc=0, scale=0.5, size=N)    # Normal com μ=0 e σ=0.5
    elif distrib_y == 'student_t':
        y = t.rvs(df=5, loc=0, scale=0.5, size=N)  # Student's t com μ=0 e σ=0.5

    # Retornar os pontos como um numpy.array
    return np.array([x, y]).T  # Transpõe para que cada linha seja um ponto (x, y)

N = 100  # Número de pontos a sortear
pontos = sortear_pontos(N, distrib_x='normal', distrib_y='uniforme')

#questão 5)

from scipy.spatial import ConvexHull

def calcular_fecho_convexo(pontos):
    # Calcular o fecho convexo
    hull = ConvexHull(pontos)
    
    # Obter os pontos que pertencem ao fecho convexo
    pontos_fecho = pontos[hull.vertices]
    
    return np.array(pontos_fecho)
print(calcular_fecho_convexo(pontos))
