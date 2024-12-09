import numpy as np


class Decomposition:
    def __init__(self, matrix):
        self.A = matrix
        self.Q = np.zeros(matrix.shape)
        self.R = np.zeros(matrix.shape)

    def dot_product(self, a, b):
        m = 0
        for i in b:
            m += b ** 2
        ans = 0
        for i in range(len(a)):
            ans += a[i] * b[i]
        return ans

    def Gram_Schmidt_orthogonalization(self):
        size = len(self.A)
        for i in range(size):
            vect = self.A[:, i]
            for j in range(i):
                vect2 = self.A[:, i - 1]
                vect -= self.dot_product(vect, vect2) * vect2
            self.A[:, i] = vect
