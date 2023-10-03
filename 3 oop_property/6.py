class StackObj:
    
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
        tmp = self.top.next
        while tmp is not None:
            if tmp.next.next == None:
                break
            tmp = tmp.next
        tmp.next = None
        
    def get_data(self):
        tmp = self.top.next
        res : list[str] = [self.top.data]
        while tmp.next is not None:
            res.append(tmp.data)
            tmp = tmp.next
        return res
    
    def push(self, obj):
        if self.top == None:
            self.top = obj
        else:
            tmp = self.top.next
            while tmp.next is not None:
                tmp = tmp.next
            else:
                tmp.next = obj