import random
import numpy as np

from decomposition import qr_decomposition


class Matrix:
    def __init__(self, size):
        self.m = np.zeros((size, size))
        self.size = size

    def rand_fill(self):
        for i in range(self.size):
            self.m[i] = [random.randint(-10, 10) for _ in range(self.size)]

    def user_fill(self):
        print(f"Введите строку матрицы (длина {self.size}). Формат ввода: a,b,c,...d")
        for i in range(self.size):
            line = [int(n) for n in input().split(',')]
            self.m[i] = line

    def near_singular(self, tol=0.1):
        print("Создается матрица")
        D = np.diag(np.random.uniform(-tol, tol, self.size))
        P, _ = qr_decomposition(np.random.rand(self.size, self.size))
        Q, _ = qr_decomposition(np.random.rand(self.size, self.size))
        A = P @ D @ Q
        self.m = A
