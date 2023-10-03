class LinkedList:
    
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def add_obj(self, obj):  # добавление нового объекта obj класса ObjList в конец связного списка;
        if self.head is None:
            self.head = obj
        obj.set_prev(self.tail)
        self.tail = obj
        if self.head is None:
            self.head = obj
        
    def remove_obj(self): #- удаление последнего объекта из связного списка;
        self.tail = self.tail.get_prev()
        self.tail.set_next(None)
        
    def get_data(self): # получение списка из строк локального свойства __data всех объектов связного списка.
        i = 0
        res = list()
        obj = self.tail
        while i is not None:
            res.append(obj.get_data())
            obj = obj.get_next()
    
    
class ObjList:
    
    _ID = -1
    
    def __new__(cls, *args, **kwargs):
        cls._ID += 1
        return super().__new__(cls)
        
    def __init__(self, data):
        self.__prev = None
        self.__next = None
        self.__data = data
        self.id = self._ID
        
    def set_next(self, obj):
        self.__next = obj
    
    def set_prev(self, obj):
        self.__prev = obj
    
    def get_next(self):
        return self.__next
    
    def get_prev(self):
        return self.__prev
    
    def set_data(self, data):
        self.__data = data
        
    def get_data(self):
        return self.__data
    
    def get_id(obj):
        return obj._ID
    
    
lst = LinkedList()
lst.add_obj(obj1 := ObjList('1'))
lst.add_obj(obj2 := ObjList('2'))
obj3 = ObjList('3')
lst.add_obj(obj3)
obj4 = ObjList('4')
lst.add_obj(obj4)
