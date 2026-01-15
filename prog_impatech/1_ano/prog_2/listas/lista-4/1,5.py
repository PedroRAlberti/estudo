primeiro vou copiar o codigo de arvore que o prof. emilio fez e colocou no github
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
    print("A árvore {ts3} não está balanceada.")#questao 1)
