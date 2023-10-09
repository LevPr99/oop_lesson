from math import sqrt

class LineTo:
    
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
        
        @property
        def x(self):
            return self.__x
        
        @x.setter
        def x(self, x):
            self.__x = x
            
        @property
        def y(self):
            return self.__y
        
        @y.setter
        def y(self, y):
            self.__y = y
        
class PathLines:
    
    def __init__(self, *line) -> None:
        self.__lines = [LineTo()]
        for l in line:
            self.__lines.append(l)
    
    def get_path(self):
        return self.__lines
    
    def get_length(self):
        res = 0
        i = 1
        while i < len(self.__lines):
            res += sqrt((self.__lines[i].x - self.__lines[i - 1].x) ** 2 + (self.__lines[i].y - self.__lines[i - 1].y) ** 2)
            i += 1
        return res
            
    def add_line(self, line):
        self.__lines.append(line)
        
        
p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length() #?