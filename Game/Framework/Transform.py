from Framework.Vector2 import *

class transform:
    def __init__(self,x = 0, y = 0):
        self.translate = vec2(x, y)
        self.rotate = 0
        self.scale = vec2(1,1)
    def __del__(self):
        pass