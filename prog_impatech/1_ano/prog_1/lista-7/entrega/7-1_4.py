#exercicio 1)
def gerar_e_salvar_ponto(a,b,c):
    #onde A é o inicial, B final e C a quantidade de pontos
    passo = (b-a)/c
    x = a
    pontos = []
    for i in range(c):
        x += passo
        y = x**8 - 3*x**4 + 2*x**3 - 2*x**2 -x + 2
        pontos.append(str(x) + " " + str(y))
    return ';'.join(pontos)
#serão salvos cada ponto em uma linha
    
pontos = gerar_e_salvar_ponto(-3/2, 3/2, 1000)
f = open('pontos.txt', 'w')
f.write(pontos)
f.close()
#aqui foram os pontos foram feitos e salvos em um arquivo chamado "pontos.txt"

import matplotlib.pyplot as plt
f = open('pontos.txt','r')
text = f.read()
f.close()
#o arquivo com os pontos foi aberto e será lido de forma que serão salvos e separados os valores de Xs e Ys
Xs = []
Ys = []
for line in text.split(';'):
    coordinates = line.split(' ')
    Xs.append(float(coordinates[0]))
    Ys.append(float(coordinates[1]))
plt.plot(Xs, Ys)
plt.show()

#exercicio 2)

a = [[1,4],[5,7],[2,3],[-1,3],[8,12]]
def merge_intervals(a):
    #primeiro criarei uma lista que ordena a lista dada pelo primeiro termo dos intervalos, ou seja, seus inícios.
    lista_ordenada = sorted(a)
    for i in range(len(lista_ordenada)-1):
        #a análise se dá em intervalos consectivos, sempre vendo se há interseção
        #caso os intervalos não tenham elementos em comum, nada acontecerá e será mantido tudo igual
        #caso os intervalos tenham elementos em comum, o próximo intervalo vai ser alterado de forma que contenha um intervalo que seja união dos 2
        if lista_ordenada[i+1][0] <= lista_ordenada[i][1]:
            lista_ordenada[i+1] = [lista_ordenada[i][0], max(lista_ordenada[i][1],lista_ordenada[i+1][1])]
            lista_ordenada[i].clear()
            #e neste caso, o intervalo em questao avaliado é esvaziado e futuramente apagado
    nao_vazios = []
    for i in lista_ordenada:
        if i != []:
            nao_vazios.append(i)
            print(i)
            # e para finalizar, são pegos os intervalos não esvaziados
    return nao_vazios    
print(merge_intervals(a))

# exercicio 3)
def missing_int(a):
    tamanho = len(a) - 1
    lim_esq = 0
    lim_dir = tamanho
    indice = tamanho // 2

    while lim_dir - lim_esq > 1:
        #é importante reitificar que ao fazer a diferença dos limites maior que 1 inclui numeros entre os da lista, pois neste momento os limites são "vizinhos"
        indice = (lim_dir + lim_esq) // 2
        #a ideia do código é compara a distancia dos indices com o valor a estes associados. 
        #é importante começar pela esquerda para se certificar que se pegue o menor valor
        if a[indice] - a[lim_esq] != indice - lim_esq:
            lim_dir = indice
            print("a", a[indice])
            continue
        if a[lim_dir] - a[indice] != lim_dir - indice:
            lim_esq = indice
    return ( a[lim_esq] + 1)
    # e obrigatoriamente o valor procurado será o próximo do numero à esquerda

#exercicio 4)
#onde primeiro há o codigo contendo a lista encadeada
class no:
    def __init__(self,valor = 0,next = None):
        self.valor = valor
        self.next_no = next

class lista_encadeada:
    def __init__(self,head):
        self.head = head
        self.len = 1
        atual = head
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
