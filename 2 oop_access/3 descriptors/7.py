class FloatValue:
    
    def __set_name__(self, owner, instance):
        self.name = '__' + instance
        
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, data: float):
        self.is_float(data)
        setattr(instance, self.name, data)
    
    @classmethod
    def is_float(cls, value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")
        
class Cell:
    
    value = FloatValue()
    
    def __init__(self, value) -> None:
        self.value = value
        
class TableSheet:
    pass