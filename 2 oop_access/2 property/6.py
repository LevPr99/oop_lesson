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
        if self.top is not None:
            tmp = self.top
        
        if tmp.next is not None:
            while tmp.next.next is not None:
                tmp = tmp.next
            tmp.next = None
        else:
            tmp = self.top
            self.top = None
            return tmp
        
    def get_data(self):
        res = list()
        if self.top is not None:
            tmp = self.top
            while tmp is not None:
                res.append(tmp.data)
                tmp = tmp.next
        return res
    
    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            tmp = self.top
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = obj

                
s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1
    
assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

s = Stack()
top = StackObj("name_1")
s.push(top)
obj = s.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"