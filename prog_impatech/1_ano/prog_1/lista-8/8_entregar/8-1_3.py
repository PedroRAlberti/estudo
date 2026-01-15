# QUESTÃO 1)
def merge_reversed_lists (a,b):
    lista_final = []
    lim1 = len(a)
    lim2 = len(b)
    aux1 = 0
    aux2 = 0
    # a ideia é criar um auxiliar para que não precise ficar passando pela lista inteira tornando a complexidade de pior caso (M + N)
    while aux1 < lim1 and aux2 < lim2:
        #primeiro é importante avaliar se algum dos auxiliares chegou ao ultimo valor das listas originais
        if aux1 == lim1:
            lista_final.append(a[aux2])
            aux2 += 1
            continue
        if aux2 == lim2:
            lista_final.append(a[aux1])
            aux1 += 1
            continue
        #após esse primeiro teste, é importante saber qual dentre os 2 números avaliados é maior, menor ou igual. tomando as atitudes apropriadas em cada caso
        if a[aux1] > b[aux2]:
            lista_final.append(a[aux1])
            aux1 += 1
            continue
        if a[aux1] < b[aux2]:
            lista_final.append(b[aux2])
            aux2 += 1
            continue
        if a[aux1] == b[aux2]:
            lista_final.append(a[aux1])
            lista_final.append(b[aux2])
            aux1 += 1
            aux2 += 1
    return lista_final
a = [10,9,8,6,5,3,2]
b = [11,9,7,5,3,2]
print(merge_reversed_lists(a,b))

# QUESTÃO 2)
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
print(is_in_previous_elements(a,b,c))

# QUESTÃO 3)
a = "()(((aaaa)))"
b = "())(()"
def validade_parenthesis(a):
    suporte = 0
    # para essa questão, são importantes tomar cuidado com 2 casos: se tiver mais parantesis abrindo do que fechando, ou vice verso. ou se tiver parantesis fechando antes do seu respectivo abrindo
    for i in a:
        if i == "(":
            suporte += 1
        if i == ")":
            suporte -= 1
            if suporte == -1:
                #esta condição avalia se durante a string há algum parantesis fechando que seu respectivo abrindo
                return False
    if suporte == 0:
        return True
    #esta condição avalia se há o mesmo número de parentesis abrindo que fechando
    return False
print(validade_parenthesis(a))
print(validade_parenthesis(b))