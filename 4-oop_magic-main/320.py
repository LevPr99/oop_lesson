from typing import Any


class FilterValidate:
    
    def __init__(self, date: int) -> None:
        self.date = date
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.name]
    
    def __set__(self, obj, value):
        obj.__dict__[self.name] = value
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        pass

  
class Mechanical(FilterValidate):
    pass

class Aragon(FilterValidate):
    pass

class Calcium(FilterValidate):
    pass


class GeyserClassic:
    
    MAX_DATE_FILTER = 100
    
    def add_filter(self, slot_num, filter):
        pass
    
    def remove_filter(self, slot_num):
        pass
    
    def get_filters(self):
        pass
    
    def water_on(self):
        pass
    
m = Mechanical(100)
print(vars(m))
m.date = 123
print(vars(m))