class Point:
    
    def __init__(self, *args):
        self.__x, self.__y = args
    
    def get_coords(self):
        return self.__x, self.__y
    
    
class Rectangle:
    
    def __init__(self, *args):
        if len(args) == 4:
            self.__sp = Point(*args[0:2]) if len(args) == 4 else args[0]
            self.__ep = Point(*args[2:4]) if len(args) == 4 else args[1]
        elif len(args) == 2:
            self.__sp = args[0]
            self.__ep = args[1]

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep
        
    def get_coords(self):
        return self.__sp, self.__ep
        
    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')
                
        
rect = Rectangle(Point(0, 0), Point(20, 34))
rect.draw()
