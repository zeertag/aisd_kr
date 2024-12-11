import random
import numpy as np


class Matrix:
    def __init__(self, size):
        self.m = np.zeros((size, size))
        self.size = size

    def rand_fill(self):
        for i in range(self.size):
            self.m[i] = [random.randint(0, 15) for _ in range(self.size)]

    def user_fill(self):
        for i in range(self.size):
            print(f"Введите строку матрицы (длина {self.size}). Формат ввода: a,b,c,...d")
            line = [int(n) for n in input().split(',')]
            self.m[i] = line
