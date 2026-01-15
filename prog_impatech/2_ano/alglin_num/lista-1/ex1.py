class matrix:
    def __init__(self, n, m): # n linhas, m colunas
        self.n = n
        self.m = m
        self.mat = [[0 for _ in range(m)] for _ in range(n)]
    
    def multiply_row(self, c, n): # multiplica a linha n por c
        for j in range(self.m):
            self.mat[n][j] *= c

    def multiply_col(self, c, n): # multiplica a coluna n por c
        for j in range(self.n):
            self.mat[m][j] *= c        

    def add_row(self, n, c, m):

    def add_col

    def swap_row

    def swap_col

    def sum_matrix

    def multiply_matrix


        