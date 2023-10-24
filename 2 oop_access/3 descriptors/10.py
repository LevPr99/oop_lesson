class Bag:
    
    def __init__(self, max_weight) -> None:
        self.max_weight
        self.things = list()
        
    @property
    def things(self):
        return self.__things
    
    def add_thing(self, thing):
        pass
    
    def remove_thing(self, indx):
        pass
    
    def get_total_weight(self):
        pass
    

class Thing:
    
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight