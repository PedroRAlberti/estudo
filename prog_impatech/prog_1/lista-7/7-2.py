a = [[1,4],[5,7],[2,3],[-1,3],[8,12]]
def merge_intervals(a):
    lista_ordenada = sorted(a)
    for i in range(len(lista_ordenada)-1):
        if lista_ordenada[i+1][0] <= lista_ordenada[i][1]:
            lista_ordenada[i+1] = [lista_ordenada[i][0], max(lista_ordenada[i][1],lista_ordenada[i+1][1])]
            lista_ordenada[i].clear()
    nao_vazios = []
    for i in lista_ordenada:
        if i != []:
            nao_vazios.append(i)
            print(i)
    return nao_vazios    
print(merge_intervals(a))