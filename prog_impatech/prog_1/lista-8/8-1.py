i = 0
j = 0
def caralho (a,b):
    lista_final = []
    while a != [] and b != []:
        if a == []:
            lista_final.append(b[0])
            b.remove(b[0])
            continue
        if b == []:
            lista_final.append(a[0])
            a.remove(a[0])
            continue

        if a[0] >= b[0]:
            lista_final.append(a[0])
            a.remove(a[0]) 
            continue
        if b[0] > a[0]:
            lista_final.append(b[0])
            b.remove(b[0])
    return lista_final

a = [14,13,12,12,10,9,8,7,6,4,3,2]
b = [20,14,5,2,2,1]
print(caralho(a,b))