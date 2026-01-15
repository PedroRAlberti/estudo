lista = ("lalala","alaele","lalale")
def caralho(a):
    suporte = ""
    aaa = len(a)
    aba = len(a[0])
    pica = False
    for i in range(aba):
        if pica:
            break
        for j in range(1,aaa):
            if lista[0][i] != lista[j][i]:
                suporte_ = i
                pica = True
                break
    for i in range(suporte_):
        suporte = suporte + (a[0][i])
    return suporte

print(caralho(lista))