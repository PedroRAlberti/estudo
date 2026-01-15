import numpy as np
import time

#neste arquivo estão as questões 1 , 2 e 3.
#questao 1)
#primeiramente a implementacao da classe myarray.
class MyArray:
    def __init__(self, vetor):
        self.size = len(vetor)
        self.vetor = np.empty(max(1, self.size), dtype=object)
        self.vetor[:self.size] = vetor

    def append(self, entrada):
        if self.size == len(self.vetor):
            new_capacity = 2 * len(self.vetor) if len(self.vetor) > 0 else 1
            new_vetor = np.empty(new_capacity, dtype=object)
            new_vetor[:self.size] = self.vetor
            self.vetor = new_vetor
        self.vetor[self.size] = entrada
        self.size += 1

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.vetor[index]

    def __repr__(self):
        return f"MyArray({list(self.vetor[:self.size])})"

    def __len__(self):
        return self.size

# agora será feita a comparacao de eficiencia por meio de um caso teste
num_elements = 100000  # Número de elementos a serem adicionados

# Testando com MyArray
my_array = MyArray([])
start_time = time.time()
for i in range(num_elements):
    my_array.append(i)
my_array_time = time.time() - start_time
print(f"Tempo com MyArray: {my_array_time:.5f} segundos")

# Testando com lista do Python
py_list = []
start_time = time.time()
for i in range(num_elements):
    py_list.append(i)
py_list_time = time.time() - start_time
print(f"Tempo com lista do Python: {py_list_time:.5f} segundos")

# pode se ver que a lista do python é mais eficiente de forma geral
# mas dado que voce pode implementar a classe my array da forma que quiser, pode ser implementada de forma que o caso especificamente desejado seja otimizado.


#questao 2)
# a classe toro basicamente vai herdar a myarray com a alteração do getitem, onde será incrementada a possibilidade do index estar fora do intervalo (0,...,n)
class Toro(MyArray):
    def __getitem__(self,index):
        return self.vetor[index%self.size]

# a seguir testes simples de uso de cada questão
initial_vector = [1, 2, 3]
my_array = MyArray(initial_vector)
print(my_array)  
my_array.append(4)
my_array.append(5)
print(my_array)  
print(my_array[2])  
print(len(my_array))  

toro = Toro([1,2,3,4,5])
print(toro[-2])
print(toro[15])
