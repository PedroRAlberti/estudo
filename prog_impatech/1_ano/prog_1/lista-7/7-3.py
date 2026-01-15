def missing_int(a):
    tamanho = len(a) - 1
    lim_esq = 0
    lim_dir = tamanho
    indice = tamanho // 2

    while lim_dir - lim_esq > 1:
        print(lim_dir)
        print(lim_esq)
        print(indice)
        indice = (lim_dir + lim_esq) // 2
        if a[indice] - a[lim_esq] != indice - lim_esq:
            lim_dir = indice
            print("a", a[indice])
            continue
        if a[lim_dir] - a[indice] != lim_dir - indice:
            lim_esq = indice
            print("b")
    return ( a[lim_esq] + 1)


lista = [1,3,4,5,6,7,8,9,10,17]
print(missing_int(lista))