class Matrix:
    def __init__(self):
        self.matrix = []
        self.size = 0

    def size_setter(self, s=-1):
        if s > 0:
            self.size = s
        else:
            
