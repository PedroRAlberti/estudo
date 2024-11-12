def fatorial(a):
    fatorial = 1
    if a > 1:
        for i in range(1,a+1):
            fatorial *= i
    return fatorial
def binomio_de_newton (a,b):
    return (fatorial(a)/(fatorial(b)*fatorial(a-b)))
def triangle_pascal(a):
    lista = [[1]]
    for i in range(1,a):
        linha = []
        for j in range(0,i+1):
            linha.append(int(fatorial(i)/(fatorial(j)*fatorial(i-j))))
        lista.append(linha)
    return lista
print(triangle_pascal(5))