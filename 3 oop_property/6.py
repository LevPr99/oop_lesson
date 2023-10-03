class Data:
    
    def __init__(self, data) -> None:
        self.next = None
        self.data = data
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next):
        self.__next = next
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
        
        
class Stack:
    
    def __init__(self) -> None:
        self.top = None
        
    def pop(self):
        while self.tmp != None:
            
            ...
    
    def get_data(self):
        tmp = self.top.next
        res = [self.top.data]
        while tmp != None:
            res.append(tmp.data)
            tmp = tmp.next
        return res
    
    def push(self, obj):
        if self.top == None:
            self.top = obj
        else:
            tmp = self.top.next
            while tmp != None:
                tmp = tmp.next
            else:
                tmp.next = obj