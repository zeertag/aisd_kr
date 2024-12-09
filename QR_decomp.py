import numpy as np


class Decomposition:
    def __init__(self, matrix):
        self.A = matrix
        self.Q = np.zeros(matrix.shape)
        self.R = np.zeros(matrix.shape)

    def find_R(self):
        self.R = np.multiply(self.Q.transpose(), self.A)
        self.R = np.round(self.R, 3)

    def Gram_Schmidt_orthogonalization(self):
        size = len(self.A)
        for i in range(size):
            vect = self.A[:, i]
            vect = vect.astype(np.float64)
            for j in range(i):
                vect2 = self.A[:, j]
                a = np.dot(vect, vect2)
                b = np.dot(vect2, vect2)
                vect -= np.multiply(vect2, (a / b))
            self.Q[:, i] = vect
        self.Q = np.round(self.Q, 3)
        self.find_R()
