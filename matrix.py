import random


class Matrix:
    def __init__(self):
        self.matrix = []
        self.size = 0

    def size_setter(self, s=-1):
        if s > 0:
            self.size = s
            '''Проработать взаимодействие с пользователем'''
        else:
            self.size = random.randint(2, 10)

    def fill_matrix(self):
        '''Мб еще реализовать ввод пользователя'''
        for i in range(self.size):
            line = [random.randint(0, 100) for _ in range(self.size)]
            self.matrix.append(line)

    def clear_data(self):
        self.matrix = []
        self.size = 0
