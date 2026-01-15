class vector3d:
    def __init__(self,coord):
        self.coord = coord
        #onde o vetor será uma lista de numeros

    def __add__(self,outro_vetor):
        novo_vetor = vector3d([0,0,0])
        for i in range(0,3):
            novo_vetor.coord[i] = self.coord[i] + outro_vetor.coord[i]
        return novo_vetor
    
    def __str__(self):
        return str(self.coord)    

    def __sub__(self,outro_vetor):
        novo_vetor = vector3d([0,0,0])
        for i in range(0,3):
            novo_vetor.coord[i] = self.coord[i] - outro_vetor.coord[i]
        return (novo_vetor)
    
    def __rmul__(self,escalar):
        novo_vetor = []
        for i in range(3):
            novo_vetor.append(escalar*self.coord[i])
        return vector3d(novo_vetor)

if __name__ == "__main__":
    v2_test = vector3d([4,5,6])
    v1_test = vector3d([1,2,3])
    print(2*v1_test)
    print(-3*v1_test)
    print(v1_test - 5*v2_test)