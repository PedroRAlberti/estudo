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

    def print(self):
        next = self.head
        while next is not None:
            print(next.val, end = "->")
            next = next.next_no


head = List_Node(1,None)
lista = Linked_List(head)
lista.adicionar_no(List_Node(3,None))
lista.adicionar_no(List_Node(5,None))
lista.adicionar_no(List_Node(7,None))
lista.print()
print(lista.self.len)

def is_palyndrome(lista):
    tamanho = lista.self.len
    #a ideia para esta funçao é utilizar o metodo "achar_valor" e comparar o termo I com o termo self.len - I
    for i in range(0,tamanho):
        if lista.achar_valor(i) != lista.achar_valor(tamanho - i):
            return False
    return True

# is_palyndrome(lista)