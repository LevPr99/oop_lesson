class RadiusVector2D:
    
    MIN_COORD = -100
    MAX_COORD = 1024
    
    def __init__(self, x = 0, y = 0) -> None:
        self.__y = 0
        self.__x = 0
        if self.check_coords(x):
            self.__y = y
        if self.check_coords(y):
            self.__x = x
    
    @classmethod
    def check_coords(cls, coord):
        return isinstance(coord, (int, float)) and (cls.MIN_COORD < coord < cls.MAX_COORD)
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if self.check_coords(x):
            self.__x = x
        
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        if self.check_coords(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.x*vector.x + vector.y*vector.y
    
v = RadiusVector2D(13, 4312331)

print(v.x, v.y)