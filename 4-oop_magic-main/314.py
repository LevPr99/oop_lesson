from abc import abstractmethod


class Validator:
    
    def __set_name__(self, owner, name):
        self.name = '__' + name
    
    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.name, value)
        
    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)
    
    @abstractmethod
    def validate(self, value):
        pass


class NumberValidator(Validator):
    
    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        if value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")


class StringValidator(Validator):
    
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        
    
class Product:
    
    __ID = 0
    id = NumberValidator()
    weight = NumberValidator()
    price = NumberValidator()
    name = StringValidator()
    
    
    def __new__(cls, *args):
        cls.__ID += 1
        return super().__new__(cls)
    
    def __init__(self, name, weight, price):
        self.id = self.__ID
        self.name = name
        self.weight = weight
        self.price = price
        
    def __delattr__(self, name):
        name = '__' + name
        if name == '__id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            super().__delattr__(name)


class Shop:
    
    name = StringValidator()
    
    def __init__(self, name):
        self.name = name
        self.goods = list()
        
    def add_product(self, product): #- добавление нового товара в магазин (в конец списка goods);
        self.goods.append(product)
    
    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)
    
    
shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
del book.name

del book.id
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
shop.remove_product(book)
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")