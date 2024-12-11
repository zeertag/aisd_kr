import random
import numpy as np


class Matrix:
    def __init__(self, size):
        self.m = np.zeros((size, size))
        self.size = size

    def rand_fill(self):
        for i in range(self.size):
            self.m[i] = [random.randint(-100, 100) for _ in range(self.size)]

    def user_fill(self):
        print(f"Введите строку матрицы (длина {self.size}). Формат ввода: a,b,c,...d")
        for i in range(self.size):
            line = [int(n) for n in input().split(',')]
            self.m[i] = line

    def near_singular(self, tol=0.5):
        print("Создается матрица")
        while True:
            self.rand_fill()
            if abs(np.linalg.det(self.m)) < abs(tol) and np.linalg.det(self.m) != 0.0:
                break
