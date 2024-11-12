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
        self.lista.pop(i)


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
