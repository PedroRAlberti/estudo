class point2D():
    def __init__(self,x,y):
        self.coord = (x,y)

    def __str__(self):
        return str(self.coord)

class polygon():
    def __init__(self,lista,cor):
        self.cor = cor
        aux = []
        for i in lista:
            aux.append(i.coord)
        self.lista = aux
        self.pontos = len(self.lista)

    def __str__(self):
        string = []
        for i in self.lista:
            string.append(str(i))
        lista = []
        lista.append(",".join(string))
        return str(str(lista) + " , " + str(self.cor))

class polygons():
    def __init__(self):
        self.len = 0
        self.poligonos = []

    def add_poligono(self,poligono,nome):
        self.len += 1
        lista = []
        lista.append(nome)
        lista.append(poligono.lista)
        lista.append(poligono.cor)
        self.poligonos.append(lista)
    
    def remove_polygon(self,nome):
        for i in range(self.len):
            if self.poligonos[i][0] == nome:
                self.poligonos.remove(self.poligonos[i])
                self.len -= 1
                return
            
    def save_to_file(self,nome):
        f = open(nome, 'w')
        for i in range(5):
            f.write(str(i))
        f.write(str(self.poligonos))
        f.close()

    def load_from_file(self,nome):
        f = open(nome,'r')
        text = f.read()
        f.close()
        self.poligonos = text
        return 

    def __str__(self):
        lista = []
        for i in range(self.len):
            lista.append(self.poligonos[i])
        return  str((lista))
    
import turtle

def desenhar_poligono(a):
    # Inicializa a tela e a caneta (turtle)
    tela = turtle.Screen()
    caneta = turtle.Turtle()
    poligonos = a.poligonos
    print(poligonos)
    for i in range(a.len):
        quantidade_de_pontos = len(poligonos[i][1])
        #este primeiro for é para desenhar cada poligono que está no objeto dado 
        # Define a cor da caneta
        caneta.color((poligonos[i][-1]))

        # Levanta a caneta para evitar desenhar linhas ao se movimentar
        caneta.penup()

        # Move para o primeiro vértice (ponto inicial)
        caneta.goto(poligonos[i][1][0])

        # Baixa a caneta para começar a desenhar
        caneta.pendown()

        # Desenha o polígono
        for j in range(quantidade_de_pontos):
            caneta.goto(poligonos[i][1][j])

        # Fecha o polígono
        caneta.goto(poligonos[i][1][0])

    # Completa o desenho
    turtle.done()

A = point2D(10,20)
B = point2D(10,50)
C = point2D(40,50)
D = point2D(40,20)
E = point2D(10,10)
poligono4 = polygon([A,B,C,D,E],"red")
poligono1 = polygon([A,B,C,D],"blue")
poligono2 = polygon([A,C,D],"orange")
poligono3 = polygon([A,C],"green")

poligonos = polygons()
poligonos.add_poligono(poligono1,"quadrado")
poligonos.add_poligono(poligono2,"triangulo")
poligonos.add_poligono(poligono3,"reta")
poligonos.add_poligono(poligono4,"pentagono")
# poligonos.remove_polygon("reta")
# print(poligonos)
poligonos.save_to_file("alb")
poligonos2 = polygons()
poligonos2.load_from_file("alb")
poligonos2.save_to_file("alb.copy")




desenhar_poligono(poligonos)