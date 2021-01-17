from abc import ABC

#Abstract Base Class
class Piece(ABC):
    def __init__(self, isCaptured, color):
        self.isCaptured = isCaptured
        self.color = color

class Wumpus(Piece):
    def __init__(self, isCaptured, color):
        super().__init__(isCaptured, color)
    def toString(self):
        return self.color + "W"

class Hero(Piece):
    def __init__(self, isCaptured, color):
        super().__init__(isCaptured, color)
    def toString(self):
        return self.color + "H"

class Mage(Piece):
    def __init__(self, isCaptured, color):
        super().__init__(isCaptured, color)
    def toString(self):
        return self.color + "M"
