class no:
    def __init__(self,valor = 0,next = None):
        self.valor = valor
        self.next_no = next

class lista_encadeada:
    def __init__(self,head):
        self.head = head
        self.len = 1
        atual = head
        # while atual:
        #     self.len += 1
        #     atual = atual.next_no

    def adicionar_no(self,val):
        self.len +=1
        if self.head is None:
            self.head = val
            return
        atual = self.head
        while atual.next_no is not None:
            atual = atual.next_no
        atual.next_no = val

    def achar_valor(self,indice):
        if indice >= self.len:
            return
        #deixando claro que a contagem está sendo iniciada pelo 0.
        #logo, caso se queira o,por exemplo, terceiro nó, o indíce deve ser 2.
        contador = 0
        atual = self.head
        while contador < indice:
            contador += 1
            atual = atual.next_no
        return atual
    
    def print(self):
        next = self.head
        while next is not None:
            print(next.valor, end = "->")
            next = next.next_no
    
def is_palyndrome(lista):
    tamanho = lista.len - 1
    #a ideia para esta funçao é utilizar o metodo "achar_valor" e comparar o termo I com o termo self.len - I
    for i in range(0,tamanho//2):
        if lista.achar_valor(i).valor != lista.achar_valor(tamanho - i).valor:
            return False
    return True
