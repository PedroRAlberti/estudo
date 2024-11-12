#a)
def potencia(x: float, n: int):
    contador = 0
    valor_final = 1
    #a ideia é fazer um loop de forma que 1 é multiplicado por "x" "n" vezes 
    if n == 0:
        return 1
    if n > 0:
        while contador < n:
            valor_final *=x
            contador += 1
    if n < 0 :
        while contador > n:
            valor_final /= x
            contador -= 1
    print(valor_final)
potencia(5,-2)