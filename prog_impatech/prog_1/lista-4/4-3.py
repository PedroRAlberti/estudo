# 1a) 
# 1
# x

# b)
# valeu is bad

# c)
# que massa!

# d)
# [1, 2, 5, 4]
# [1,2,3,4]

# 2a)
# mudar o "inst" para "init"

# b)
# []
# [2.0, 1.0]

# c) 
# as entradas dos vetores estao com mesmo nome, impossibilitando a maquina de entender o que executar. eu usaria dentro do metodo adicionaria um outro nome que possibilitasse a maquina de entender o que lhe é pedido. como por exemplo other_vector.value(i)

# questao 3.a)

class circle:
    #primeiro defini o ponto avaliado e o raio da circunferencia de centro na origem
    def __init__(self,raio):
        self.raio = raio
    #para saber a posicao relativa entre um ponto e uma circunferencia basta saber se o módulo da distancia do ponto ao centro é maior,igual ou menor que o raio
    def posicao_relativa(self,x,y):
        self.x = x
        self.y = y
        if ((self.x**2)+(self.y**2)) > self.raio**2:
            print("está fora da circunferencia")
        elif ((self.x**2)+(self.y**2)) == self.raio**2:
            print("o ponto está sobre a circunferencia")
        else:
            print("está dentro da circunferencia")
#questao 3.b)
class line_segment:
    def __init__(self,x1,y1,x2,y2):
        # sendo os 2 primeiros pontos definidores do segmento e o terceiro o avaliado
        if x1 > x2:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
        if x1 < x2:
            self.x2 = x1
            self.y2 = y1
            self.x1 = x2
            self.y1 = y2
        #primeiro precisa ser definido se os 3 pontos estão numa mesma reta, que é calculado pelo det = 0
    def posicao(self,x3,y3):
        self.x3 = x3
        self.y3 = y3
        if x1 == x2:
            if y1 > y2:
                if y3 < y1 and y3 > y2:
                    return True
            if y1 < y2:
                if y3 > y1 and y3 < y2:
                    return True
            return False
        determinante = self.x1*self.y2 + self.x2*self.y3 + self.x3*self.y1 - (self.y1*self.x2 + self.y2*self.x3 + self.x1*self.y3) 
        #mas também restaria o caso onde pertence a reta a não ao segmento, para isso basta analisar qualquer coordenada dentro dos pontos
        if self.x3>=self.x2 and self.x3<=self.x1:
            if  determinante  == 0:
                return True
        return False

# #4)
circle_1 = circle(5)
line_1 = line_segment()
def funcao(circulo,segmento):
   if (segmento.x1**2 + segmento.y1**2) <= (circulo.raio**2) and (segmento.x2**2 + segmento.y2**2) <= (circulo.raio**):
       return True
   return False
# #5)

class vector():
    def __init__(self,list1):
        self.list1 = list1 
    def d(self, vetor2):
        prod_final = []
        prod_int = []
        for i in self.list1:
            prod_int = []
            for j in vetor2.list1:
                prod_int.append(i*j)
            prod_final.append(prod_int.copy())
        print(prod_final)
u = vector([1,2])
v = vector([1,2,3])
u.d(v)