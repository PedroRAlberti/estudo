#pela descricao da questao, vou somente fazer um codigo que identifique o epsilon
x = 1
y = 2
while y != 1:
    y = 1
    x /= 1.0001
    y -= x 

print (x)

x = 1
y = 2
while y != 10**6:
    y = 10**6
    x /= 1.0001
    y -= x 

print (x)

