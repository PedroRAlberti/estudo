#a questao 1 vai da linha 2 até a 24 , a questão 2 e 3 de 26 a 290 e a questão 5 de 292 até 316

#questão 1)
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

#questao 2 e 3)
# as modificações pedidas no item 2 foram implementadas diretamente no vector 2D
# enquanto as pedidas no item 3 foram criadas e implementadas nos vector 3D e polinomio
class VectorSpace:
    """VectorSpace:
    Abstract Class of vector space used to model basic linear structures
    """
    
    def __init__(self, dim: int, field: 'Field'):
        """
        Initialize a VectorSpace instance.

        Args:
            dim (int): Dimension of the vector space.
            field (Field): The field over which the vector space is defined.
        """
        self.dim = dim
        self._field = field
        
    def getField(self):
        """
        Get the field associated with this vector space.

        Returns:
            Field: The field associated with the vector space.
        """
        return self._field
    
    def getVectorSpace(self):
        """
        Get a string representation of the vector space.

        Returns:
            str: A string representing the vector space.
        """
        return f'dim = {self.dim!r}, field = {self._field!r}'
        # return self.__repr__()

    def __repr__(self):
        """
        Get a string representation of the VectorSpace instance.

        Returns:
            str: A string representing the VectorSpace instance.
        """
        # return f'dim = {self.dim!r}, field = {self._field!r}'
        return self.getVectorSpace()
    
    def __mul__(self, f):
        """
        Multiplication operation on the vector space (not implemented).

        Args:
            f: The factor for multiplication.

        Raises:
            NotImplementedError: This method is meant to be overridden by subclasses.
        """
        raise NotImplementedError
    
    def __rmul__(self, f):
        """
        Right multiplication operation on the vector space (not implemented).

        Args:
            f: The factor for multiplication.

        Returns:
            The result of multiplication.

        Note:
            This method is defined in terms of __mul__.
        """
        return self.__mul__(f)
    
    def __add__(self, v):
        """
        Addition operation on the vector space (not implemented).

        Args:
            v: The vector to be added.

        Raises:
            NotImplementedError: This method is meant to be overridden by subclasses.
        """
        raise NotImplementedError

class RealVector(VectorSpace):
    _field = float
    def __init__(self, dim, coord):
        super().__init__(dim, self._field)
        self.coord = coord
    

    @staticmethod
    def _builder(coord):
        raise NotImplementedError


    def __add__(self, other_vector):
        n_vector = []
        for c1, c2 in zip(self.coord, other_vector.coord):
            n_vector.append(c1+c2)
        return self._builder(n_vector)


    def __mul__(self, alpha):
        n_vector = []
        for c in self.coord:
            n_vector.append(alpha*c)
        return self._builder(n_vector)
    
    
    def iner_prod(self, other_vector):
        res = 0
        for c1, c2 in zip(self.coord, other_vector.coord):
            res += c1*c2
        return res


    def __str__(self):
        ls = ['[']
        for c in self.coord[:-1]:
            ls += [f'{c:2.2f}, ']
        ls += f'{self.coord[-1]:2.2f}]'
        s =  ''.join(ls)
        return s

# foram adicionadas as substrações e abs como o módulo
class Vector2D(RealVector):
    _dim = 2
    def __init__(self, coord):
        if len(coord) != 2:
            raise ValueError
        super().__init__(self._dim, coord)

    def __sub__(self,other_vector):
        new_vector = []
        for c1,c2 in zip(self.coord,other_vector.coord):
            new_vector.append(c1 - c2)
        return self._builder(new_vector)
    
    def __abs__(self):
        #abs ou norma foi interpretado como a norma 2 (modulo do vetor)
        norma = 0
        for c in (self.coord):
            norma += c**2
        return (norma**(1/2))

    @staticmethod
    def _builder(coord):
        return Vector2D(coord)
    

    def CW(self):
        return Vector2D([-self.coord[1], self.coord[0]])
    

    def CCW(self):
        return Vector2D([self.coord[1], -self.coord[0]])
    
#na classe 3D foram implementadas os mesmos metodos que no vector 2D
class Vector3D(RealVector):
    _dim = 3
    def __init__(self, coord):
        if len(coord) != 3:
            raise ValueError
        super().__init__(self._dim, coord)

    def __sub__(self,other_vector):
        new_vector = []
        for c1,c2 in zip(self.coord,other_vector.coord):
            new_vector.append(c1 - c2)
        return self._builder(new_vector)
    
    def __abs__(self):
        #abs ou norma foi interpretado como a norma 2 (modulo do vetor)
        norma = 0
        for c in (self.coord):
            norma += c**2
        return (norma**(1/2))

    @staticmethod
    def _builder(coord):
        return Vector3D(coord)
    
# a classe polinomio foi feita de forma que fosse escrito no formato de um vetor e tem módulos de soma e subtração    
class Polinomio(RealVector):
    #o polinomio deve ser escrito no formato de vetor, com base que a primeira entrada é o coeficiente de grau n e o último o coeficiente de grau 0
    def __init__(self,coord):
        self._dim = len(coord)
        super().__init__(self._dim,coord)

    @staticmethod
    def getVectorSpace(self):
        return f'dim = {self.dim!r}, field = {self._field!r}'

    @staticmethod
    def _builder(coord):
        return Polinomio(coord)
#a soma e subtração deve se ter um cuidado a mais para quando os polinomios tem dimensão diferente.     
    
    def __add__(self,other_polinomio):
        new_vector = []
        if self._dim == other_polinomio._dim:
            return super().__add__(other_polinomio) 
        if self._dim != other_polinomio._dim:
            menor_dim = min(self._dim,other_polinomio._dim)
            maior_dim = max(self._dim,other_polinomio._dim)
            if self._dim < other_polinomio._dim:
                aux = True
            else: aux = False

            for c in range(menor_dim):
                new_vector.append(self.coord[c] + other_polinomio.coord[c])
        
            if aux == True:
                for c in range(menor_dim,maior_dim):
                    new_vector.append(other_polinomio.coord[c])
            if aux == False:
                for c in range(menor_dim,maior_dim):
                    new_vector.append(self.coord[c])
            return new_vector   
        
    def __sub__(self,other_polinomio):
        new_vector = []
        if self._dim == other_polinomio._dim:
            for c in range(self._dim):
                new_vector.append(self.coord[c] - other_polinomio.coord[c])
            return new_vector
        if self._dim != other_polinomio._dim:
            menor_dim = min(self._dim,other_polinomio._dim)
            maior_dim = max(self._dim,other_polinomio._dim)
            if self._dim < other_polinomio._dim:
                aux = True
            else: aux = False

            for c in range(menor_dim):
                new_vector.append(self.coord[c] - other_polinomio.coord[c])
        
            if aux == True:
                for c in range(menor_dim,maior_dim):
                    new_vector.append(other_polinomio.coord[c])
            if aux == False:
                for c in range(menor_dim,maior_dim):
                    new_vector.append(self.coord[c])
            return new_vector

if __name__ == '__main__':
    V2 = Vector2D([1, 2])
    W2 = Vector2D([3, 4])
    V3 = Vector3D([1,2,3])
    W3 = Vector3D([5,4,6])
    y = Polinomio([1,2,4])
    X = Polinomio([0,1,4,5,6])

    print(V3.getVectorSpace())
    z = X-y
    print(z)
    r = V3+4*W3
    s = W2-3*V2
    print(abs(V3))
    print(s)
    print('V2 + 4*W2 =', r)
    print('V2.iner_prod(W2) = ', V3.iner_prod(W3))

#questão 5)
# o problema inicial era que deveriam estar sendo embaralhadas a instancia de cartas do baralho
import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

#um print antes e depois de embaralhar
myDeck = FrenchDeck()
print(myDeck[1])  
random.shuffle(myDeck._cards)
print(myDeck[1])