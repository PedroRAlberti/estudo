def dict_to_string(a):
    polinomio = ""
    # ordena as chaves, expoentes, e inverte
    expoentes = sorted(list(a.keys()), reverse=True)
    for i in expoentes:
        #passa pelos coeficientes
        coeficiente = a[i]
        if coeficiente > 0:
            polinomio += "+"
        polinomio += str(coeficiente)
        #esta parte serviu para que os coeficientes positivos recebessem devidamente o sinal + que está implicito no dicionario
        #de forma geral, há 3 casos: se o expoente é 0 deve ser adicionado somente o numero. se for 1, somente o coeficiente e "x". e os demais, devem ter o coeficiente, o "x" e o "^{expoente}"
        if i == 0:
            continue
        polinomio += "x"
        if i == 1:
            continue
        polinomio += f"^{i}"
    return polinomio
print(dict_to_string({3: 2, 2: -6, 1: 1, 0: -5}))