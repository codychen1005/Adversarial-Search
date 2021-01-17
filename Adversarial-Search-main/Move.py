class Move():
    def __init__(self, x_src, y_src, x_dest, y_dest, heuristic_value, alpha, beta):
        self.x_src = x_src
        self.y_src = y_src
        self.x_dest = x_dest
        self.y_dest = y_dest
        self.heuristic_value = heuristic_value
        self.alpha = alpha
        self.beta = beta

    def __lt__(self, other):
        selfPriority = self.heuristic_value
        otherPriority = other.heuristic_value
        return selfPriority < otherPriority
