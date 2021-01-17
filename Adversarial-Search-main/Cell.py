class Cell():
    def __init__(self, x, y, piece, isPit):
        self.x = x
        self.y = y
        self.piece = piece
        self.isPit = False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
