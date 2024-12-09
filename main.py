import numpy as np

from matrix import Matrix
from QR_decomp import Decomposition


class QR:
    def __init__(self):
        self.A = None
        self.Q = None
        self.R = None

    def set_data_A(self, size=-1):
        m = Matrix()
        m.size_setter(size)
        self.A = np.array(m.matrix)

    def set_data_QR(self):
        QRd = Decomposition(self.A)
        QRd.Gram_Schmidt_orthogonalization()
        self.Q = QRd.Q
        self.R = QRd.R

    def algorithm(self):
        tol = 1e-10
        for i in range(30):
            self.A = np.multiply(self.R, self.Q)
            self.set_data_QR()

            print(self.A)


a = QR()
a.set_data_A()
a.set_data_QR()
a.algorithm()
