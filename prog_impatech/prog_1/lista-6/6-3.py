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

lista.delete_no(5)
lista.print()

