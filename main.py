import random
import numpy as np

from matrix import Matrix

np.set_printoptions(suppress=True)


class QR:
    def __init__(self, matrix_size=(0, 0)):
        self.A = None
        if matrix_size != (0, 0):
            self.size = matrix_size
        else:
            self.size = random.randint(2, 10)
        self.Q = np.zeros((self.size, self.size))
        self.R = np.zeros((self.size, self.size))

    def set_A(self, var=0):
        matr = Matrix(self.size)
        if var != 0:
            matr.user_fill()
        else:
            matr.rand_fill()
        self.A = matr.m

    def QR_decomposition(self):
        '''Ортогонализация Грама-Шмидта'''
        self.R = np.zeros(self.A.shape)
        self.Q = np.zeros(self.A.shape)
        for i in range(self.size):
            # Инициализация вектора v как столбца из A
            v = self.A[:, i]
            for j in range(i):
                self.R[j, i] = np.dot(self.Q[:, j], v)  # Проекция v на Q[:, j]
                v -= self.R[j, i] * self.Q[:, j]  # Вычитание проекции

                # Нормализация
            self.R[i, i] = np.linalg.norm(v)
            if self.R[i, i] == 0:
                raise ValueError("Матрица содержит линейно зависимые столбцы.")
            self.Q[:, i] = v / self.R[i, i]

    def QR_algorithm(self, max_iteration=1000, tol=1e-10):
        for i in range(max_iteration):
            # self.Q, self.R = np.linalg.qr(self.A)
            self.QR_decomposition()
            A_next = self.R @ self.Q
            if np.allclose(self.A, A_next, atol=tol):
                print('ГООООООООООООООООЛ')
                break
            self.A = A_next
        else:
            print("Выполнено максимальное количество итераций")
        return self.A


a = QR(5)
a.set_A(1)
B = np.copy(a.A)
# a.QR_decomposition()
A = a.QR_algorithm()
print(B)
print()
print(A)
print(np.diag(A))
