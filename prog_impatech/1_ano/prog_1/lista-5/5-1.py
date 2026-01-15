class no():
    def __init__(self,valor,next):
        self.valor = valor
        self.next_no = next

class lista_encadeada():
    def __init__(self,head):
        self.head = head
        self.len = 1
    def adicionar_no(self,no):
        self.len += 1
        if self.head is None:
            self.head = no
            return
        next = self.head
        while next.next_no is not None:
            next = next.next_no
        next.next_no = no
    def achar_valor (self,indice):
        if indice > self.len:
            return None
        contador = 1
        next = self.head
        while contador < indice:
            next = next.next_no
            contador += 1
        return next.valor
    def inverter(self):
        lista_invertida = lista_encadeada(no(self.achar_valor(self.len),None))
        contador = 1
        while contador < self.len:
            lista_invertida.adicionar_no(no(self.achar_valor(self.len - contador),None))
            contador += 1
        return lista_invertida
    def print(self):
        next = self.head
        while next is not None:
            print(next.valor, end = "->")
            next = next.next_no
        print("a")
        
    
head = no(1,None)
lista = lista_encadeada(head)
lista.adicionar_no(no(3,None))
lista.adicionar_no(no(5,None))
lista.adicionar_no(no(7,None))
# lista.inverter().print()
lista_teste1 = lista_encadeada(None)
# print("")
lista_teste1.print()