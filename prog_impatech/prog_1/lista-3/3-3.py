def let(a):
    vogais = ["a","e","i","o","u"]
    list = []
    for i in a:
        for j in vogais:
            if i == j: 
                list.append(i)
                vogais.remove(j)
    return list
a = "a gata do carlos"
print(let(a))