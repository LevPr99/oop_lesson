from typing import Any


class Circle:
    
    def __init__(self, x, y, radius) -> None:
        self.__x = x
        self.__y = y
        self.__radius = radius
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value
        
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
    
    def __getattribute__(self, __name: str) -> Any:
        return super().__getattribute__(__name)
    
    def __getattr__(self, name):
        return False
        
    def __setattr__(self, __name: str, __value: Any) -> None:
        names = ('_Circle__y', '_Circle__x', '_Circle__radius', 'x', 'y', 'radius')
        if __name in names:
            if isinstance(__value, (int, float)):
                super().__setattr__(__name, __value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif __name not in names:
            pass
        else:
            super().__setattr__(__name, __value)

c = Circle(123, 123, 22.22)
print(vars(c))
c.y = 312
c.name = 1
print(vars(c))
c.y = 1244
print(vars(c))
c.radius = -10
print(vars(c))
