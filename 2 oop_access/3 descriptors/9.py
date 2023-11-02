class SuperShop:
    
    def __init__(self, name) -> None:
        self.name = name
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)
    
    def remove_product(self, product):
        self.goods.pop(self.goods.index(product))


class StringValue:
    
    def __set_name__(self, owner, name):
        self.name = '__' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.name, value)
    
    @staticmethod
    def validate(value, min_length=2, max_length=50):
        return isinstance(value, str) and (min_length <= len(value) <= max_length)


class PriceValue:
    
    def __set_name__(self, owner, name):
        self.name = '__' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.name, value)
    
    @staticmethod
    def validate(value, min_length=0, max_length=10000):
        return isinstance(value, int) and (min_length <= value <= max_length)


class Product:
    
    name = StringValue()
    price = PriceValue()
    
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price