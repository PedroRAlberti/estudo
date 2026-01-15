# questao 1)
def search(a,valor):
    extr_esq = 0
    extr_dir = len(a) -1
    indice = (extr_esq + extr_dir) // 2      
    while (extr_dir - extr_esq > 1) and a[indice] != valor:
        if a[indice] > valor:
            extr_dir = indice 
        if a[indice] < valor:
            extr_esq = indice 
        indice = (extr_dir + extr_esq) // 2
        #a busca binaria normal, mas para o caso do valor nao estar na lista, quando os extremos chegarem a vizinho pois o valor está no meio, este adicionar o lugar do meio
    if a[indice] == valor:
        return indice
    else: 
        return indice + 1

#questao 2)
def fatorial(a):
    fatorial = 1
    if a > 1:
        for i in range(1,a+1):
            fatorial *= i
    return fatorial
#como planejo fazer por binomio de newton, ter uma funcao de fatorial me adiantará alguns passos
def triangle_pascal(a):
    lista = [[1]]
    for i in range(1,a):
        linha = []
        # o primeiro for serve para pegar as A linhas, o segundo entra e faz linha por linha usando o binomio de newton
        for j in range(0,i+1):
            linha.append(int(fatorial(i)/(fatorial(j)*fatorial(i-j))))
        lista.append(linha)
    return lista
# este código é n^3, pois a funcao fatorial é O(n), e está dentro de um for dentro de outro for. resultando em O(n^3)
print(triangle_pascal(5))

#questao 3)
class List_Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next_no = next

class Linked_List:
    def __init__ (self,head):
        self.head = head
        self.len = 1
        next = head
        while next:
            self.len += 1
            next = next.next_no
        #esta funcao percorre o objeto onde cada nó que passa adiciona 1 ao tamanho. Onde ao chego ao final, tem-se o tamanho total da lista

    def adicionar_no(self,no):
        if self.head is None:
            self.head = no
            return
        next = self.head
        while next.next_no is not None:
            next = next.next_no
        next.next_no = no

    def delete_no(self,valor):
        next = self.head.next_no
        atual = self.head
        while next is not None:
            if next.val == valor:
                atual.next_no = next.next_no
                break
            atual = next
            next = next.next_no
        # a ideia é que o nó ao saber que o próximo será o do valor a ser retirado, este pulará o do valor a ser retirado e terá como next o outro

    def print(self):
        next = self.head
        while next is not None:
            print(next.val, end = "->")
            next = next.next_no

#questao 4)
def converter_polinomio_para_dicionario(expressao_polinomio: str) -> dict:
    termos_polinomio = {}  
    termo_atual = ""  
    # percorre cada caractere na expressão do polinômio
    for indice in range(len(expressao_polinomio) + 1):
        if indice < len(expressao_polinomio):
            caractere_atual = expressao_polinomio[indice]  
        else:
            caractere_atual = None  
        
        # verifica se um novo termo deve ser iniciado 
        if caractere_atual is None or caractere_atual in '+-':
            if termo_atual:  
                # determina o coeficiente e o expoente do termo atual baseado no modelo dado
                if 'x' not in termo_atual:  # Termo constante (grau 0)
                    coeficiente = int(termo_atual)
                    expoente = 0
                elif '^' not in termo_atual:  # Termo de grau 1 (ex: 3x)
                    parte_coeficiente = termo_atual[:-1]  # Remove o 'x' do final
                    if parte_coeficiente and parte_coeficiente not in ('+', '-'):
                        coeficiente = int(parte_coeficiente)
                    else:
                        coeficiente = int(parte_coeficiente + '1')
                    expoente = 1
                else:  # termo de grau n (ex: 2x^3)
                    parte_coeficiente, parte_expoente = termo_atual.split('x^')
                    if parte_coeficiente and parte_coeficiente not in ('+', '-'):
                        coeficiente = int(parte_coeficiente)
                    else:
                        coeficiente = int(parte_coeficiente + '1')
                    expoente = int(parte_expoente)
                
                # Adiciona o coeficiente ao expoente correspondente no dicionário de termos do polinômio
                termos_polinomio[expoente] = coeficiente
                
            termo_atual = caractere_atual if caractere_atual else ""  # Inicia o novo termo
        else:
            termo_atual += caractere_atual
    
    return termos_polinomio

#questao 5)
def dict_to_string(a):
    polinomio = ""
    # ordena as chaves, expoentes, e inverte
    expoentes = sorted(list(a.keys()), reverse=True)
    for i in expoentes:
        #passa pelos coeficientes
        coeficiente = a[i]
        if coeficiente > 0:
            polinomio += "+"
        polinomio += str(coeficiente)
        #esta parte serviu para que os coeficientes positivos recebessem devidamente o sinal + que está implicito no dicionario
        #de forma geral, há 3 casos: se o expoente é 0 deve ser adicionado somente o numero. se for 1, somente o coeficiente e "x". e os demais, devem ter o coeficiente, o "x" e o "^{expoente}"
        if i == 0:
            continue
        polinomio += "x"
        if i == 1:
            continue
        polinomio += f"^{i}"
    return polinomio