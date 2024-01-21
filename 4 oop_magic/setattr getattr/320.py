import time

class FilterValidate:
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.name]
    
    def __set__(self, obj, value):
        if self.name in obj.__dict__:
            pass
        else:
            obj.__dict__[self.name] = value


class Filter:
    
    date = FilterValidate()
    
    def __init__(self, date):
        self.date = date
        
    def __setattr__(self, name, value):
        if name in vars(self):
            pass
        else:
            super().__setattr__(name, value)

  
class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    
    MAX_DATE_FILTER = 100
    
    def __init__(self):
        self.slots = [None for _ in range(3)]
    
    def add_filter(self, slot_num, filter):
         
        def insert(self, slot_num, filter):
            self.slots[slot_num - 1] = filter
            
        if filter not in self.slots:
            if slot_num == 1 and isinstance(filter, Mechanical):
                insert(self, slot_num, filter)
            elif slot_num == 2 and isinstance(filter, Aragon):
                insert(self, slot_num, filter)
            elif slot_num == 3 and isinstance(filter, Calcium):
                insert(self, slot_num, filter)
    
    def remove_filter(self, slot_num):
        leght = len(self.slots)
        if 0 <= slot_num - 1 < leght:
            self.slots[slot_num - 1] = None
    
    def get_filters(self):
        return tuple(i for i in self.slots if i is not None)
    
    def water_on(self):
        filters = self.get_filters()
        res = list()
        for i in filters:
            if 0 < time.time() - i.date > self.MAX_DATE_FILTER:
                res.append(False)
            else:
                res.append(True)
        return all(res) and len(filters) == 3
    
m = Mechanical(time.time())

g = GeyserClassic()
g.add_filter(1, m)
g.add_filter(2, Aragon(time.time()-99))
g.add_filter(3, Calcium(time.time()))
# g.remove_filter(3)

print(g.get_filters())
print(g.water_on())