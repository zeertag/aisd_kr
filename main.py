import random
import numpy as np
import time

from matrix import Matrix

np.set_printoptions(suppress=True)


class QR:
    def __init__(self):
        self.A = None
        self.Q = None
        self.R = None
        self.size = 0

    def set_data(self, matrix_size=0, var=0):
        if matrix_size != 0:
            self.size = matrix_size
        else:
            self.size = random.randint(2, 10)
        self.Q = np.zeros((self.size, self.size))
        self.R = np.zeros((self.size, self.size))

        matr = Matrix(self.size)
        if var == 1:
            matr.user_fill()
        elif var == 2:
            # tol = int(input("Максимальный размер определителя: "))
            matr.near_singular()
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
                print("------------------------------------------")
                print(self.A)
                # raise ValueError("Матрица содержит линейно зависимые столбцы.")
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


times = []
a = QR()
# for i in range(100):
a.set_data(3, 1)
B = np.copy(a.A)
print(np.linalg.det(B))
# a.QR_decomposition()
start = time.time()
A = a.QR_algorithm()
end = time.time()
times.append(end - start)
print(B)
print()
print(np.round(A, 5))
print()
print(np.round(np.diag(A), 5))

print(times)
# -93,0,-71
# -52,0,87
# -16,0,52

# -28, 94, 28
# 96, -87, -96
# 17, -65, -17