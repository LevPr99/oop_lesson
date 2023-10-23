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
    
    def __init__(self, value=0.0) -> None:
        self.value = value
        
class TableSheet:
    
    def __init__(self, N, M) -> None:
        self.cells = list()
        for i in range(N):
            self.cells.append([])
            for _ in range(M):
                self.cells[i].append(Cell())
        
table = TableSheet(5, 3) #?
c = 1.0
for i in table.cells:
    for j in i:
        j.value = c
        c += 1.0