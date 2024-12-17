import random
import numpy as np
import time

from matrix import Matrix
from graphs import make_graphs
from decomposition import qr_decomposition

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
            matr.near_singular()
        else:
            matr.rand_fill()
        self.A = matr.m

    def QR_algorithm(self, max_iteration=1000, tol=1e-10):
        for i in range(max_iteration):
            self.Q, self.R = qr_decomposition(self.A)
            A_next = self.R @ self.Q
            if np.allclose(self.A, A_next, atol=tol):
                break
            self.A = A_next
        else:
            print("Выполнено максимальное количество итераций")
        return self.A

#
# times = []
# a = QR()
# tests = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for size in tests:
#     t = 0
#     for i in range(10):
#         a.set_data(size, 2)
#         B = np.copy(a.A)
#         start = time.time()
#         A = a.QR_algorithm()
#         end = time.time()
#         t += end - start
#         print(np.round(np.diag(A), 5), "- собственные числа")
#     times.append(t / 10)
# make_graphs(tests, times)
#
# with open("Test_data/times.txt", "w", encoding="utf-8") as file:
#     file.write("Зависимость скорости выполнения QR алгоритма, от размера матрицы:\n\n")
#     for i in range(len(tests)):
#         file.write(f"{tests[i]} элементов: {times[i]} секунд\n")
