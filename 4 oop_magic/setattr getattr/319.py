from typing import Any


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
    
    def __init__(self, a, b, c) -> None:
        self.__a = a
        self.__b = b
        self.__c = c
        
    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, value):
        self.__a = value
        
    @property
    def b(self):
        return self.__b
    
    @b.setter
    def b(self, value):
        self.__b = value
        
    @property
    def c(self):
        return self.__c
    
    @c.setter
    def c(self, value):
        self.__c = value
    
    def check_value(self, value):
        return self.MIN_DIMENSION <= value <= self.MAX_DIMENSION
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ('_Dimensions__a', '_Dimensions__b', '_Dimensions__c', 'a', 'b', 'c') and self.check_value(__value):
            super().__setattr__(__name, __value)
        elif __name in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")


d = Dimensions(10.5, 20.1, 30)
d.a = 100
d.b = 1020
# d.MAX_DIMENSION = 10
print(vars(d))