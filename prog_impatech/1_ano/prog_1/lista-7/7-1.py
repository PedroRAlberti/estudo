def gerar_e_salvar_ponto(a,b,c):
    #onde A é o inicial, B final e C a quantidade de pontos
    passo = (b-a)/c
    x = a
    pontos = []
    for i in range(c):
        x += passo
        y = x**8 - 3*x**4 + 2*x**3 - 2*x**2 -x + 2
        pontos.append(str(x) + " " + str(y))
    return ';'.join(pontos)
#serão salvos cada ponto em uma linha
    
pontos = gerar_e_salvar_ponto(-3/2, 3/2, 1000)
f = open('pontos.txt', 'w')
f.write(pontos)
f.close()
#aqui foram os pontos foram feitos e salvos em um arquivo chamado "pontos.txt"

import matplotlib.pyplot as plt
f = open('pontos.txt','r')
text = f.read()
f.close()
#o arquivo com os pontos foi aberto e será lido de forma que serão salvos e separados os valores de Xs e Ys
Xs = []
Ys = []
for line in text.split(';'):
    coordinates = line.split(' ')
    Xs.append(float(coordinates[0]))
    Ys.append(float(coordinates[1]))
plt.plot(Xs, Ys)
plt.show()