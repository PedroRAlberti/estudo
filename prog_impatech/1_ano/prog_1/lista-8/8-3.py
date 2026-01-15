a = "()(((aaaa)))"
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
print(caralho(a))
        