lista = (1,1,2,2,3,4,4)
def achar_o_numero_isolado(a):
    #o uso do dicionario permite acessar especificamente aquela chave permitindo assim o código ter O(n)
    dict = {} 
    for i in a:
        #caso o numero já esteja no dicionário ele retira esta chave e caso não cria e dar valor 1. pois assim o único restante é aquele que só aparece uma vez
        if i not in dict:
            dict[i] = 1
        else:
            dict.pop(i)
    return list(dict.keys())[0]
print(achar_o_numero_isolado(lista))