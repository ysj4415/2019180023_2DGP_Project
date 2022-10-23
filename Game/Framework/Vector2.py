class vec2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __del__(self):
        pass

    def __add__(self, other):
        sum = vec2()
        sum.x = self.x + other.x
        sum.y = self.y + other.y
        return sum

    def set(self,x,y):
        self.x = x
        self.y = y
