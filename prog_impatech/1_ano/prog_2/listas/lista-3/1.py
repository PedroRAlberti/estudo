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
        self.epsilon = 1e8
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

class Vector3D(RealVector):
    _dim = 3
    def __init__(self, coord):
        if len(coord) != 3:
            raise ValueError
        super().__init__(self._dim, coord)
        self.epsilon = 1e-16

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
    
    def __eq__(self,other_vector):
        for i in range(3):
            if abs(self.coord[i] - other_vector.coord[i]) > self.epsilon:
                return False
        return True
    
    def __lt__(self,other_vector):
        return abs(other_vector) - abs(self) > self.epsilon
    
    def __le__(self,other_vector):
        return abs(other_vector) - abs(self) >= -(self.epsilon)
    
    def __gt__(self,other_vector):
        return abs(other_vector) - abs(self) < self.epsilon
    
    def __ge__(self,other_vector):
        return abs(other_vector) - abs(self) <= self.epsilon

    
        
    @staticmethod
    def _builder(coord):
        return Vector3D(coord)

if __name__ == '__main__':
    # o epsilon usado foi escolhida arbitrariamente como 1e-16
    V3 = Vector3D([1,2,3])
    Z3 = Vector3D([1,2,3])
    W3 = Vector3D([5,4,6])
    print (Z3 == V3)
    print (W3 >= V3)
    print (Z3 >= V3)
    print ((abs(V3) - abs(Z3)) < 1e-16)

#para as questoes 3 e 4 será feita uma funcao que pega o epsilon de delta em torno de um valor dado x
def get_epsilon(x):
    x_copy = x
    y = 0
    while y != x:
        y = x
        x_copy /= 1.0001
        y -= x_copy
    return x_copy

print(get_epsilon(1))
print(get_epsilon(1000000))

#nota-se que em cada caso, há 17 casas de notacao, então cabem mais alguns rapidos testes a fim de comprovar os dados analisados.

print(get_epsilon(10))
print(get_epsilon(1000))

#percebe-se que realmente há 17 casas de notacao.
#ou seja, o epsilon de delta ao redor de um número x tem por ordem de grandeza 17 - (ordem de grandeza do x)