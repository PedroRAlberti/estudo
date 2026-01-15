# a ideia central é que o total de casos são as permutações de cada combinacao possível
# fiz as funões de fatorial e anagrama (para permutacao) para me auxiliar futuramente
def fatorial(a):
    x = 1  
    for i in range(1,a+1):
        x *= i 
    return x

def anagrama(a,b):
    x = fatorial(a)
    y = fatorial(b)
    z = fatorial(a+b)
    return (z/(x*y))
# inicialmente ele pode subir n vezes 1 por 1, mas a cada vez ele pode "tirar 2" do 1 por 1 e acrescentar 1 no 2 por 2. e ai para cada combinacao possivel analisar as permutacoes viáveis.
def degrau(n):
    d = 0
    resultado = 0
    while n >= 0:
        k = anagrama(n,d)
        resultado += k
        d += 1
        n -= 2
    return resultado