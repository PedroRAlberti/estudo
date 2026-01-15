def is_in_previous_elements(a,b,c):
    # "a" é o numero de itens na lista, "b" o numero em que se leva em conta antes de comprar e "c" a lista propriamente
    lista = []
    contador = 0
    #caso o numero de itens que se leva em conta seja maior que o numero de itens na lista, todos os itens serao comprados
    if a <= b:
        return a
    #a ideia basicamente é que ao preencher a lista dos que se leva em conta, sempre que se acha um item que será comprado, ele será adicionado na e o primeiro item da lista será removido, e toda vez que se adiciona um item, o contador é somado 1, bastando assim retornar o contador
    for i in range (a):
        if len(lista) == b:
            if c[i] not in lista:
                lista.append(c[i])
                contador += 1
                lista.remove(lista[0])
            continue
        lista.append(c[i])
        contador += 1
    return contador
a = 10
b = 3
c = [1,2,3,4,5,5,4,3,2,1]
is_in_previous_elements(a,b,c)