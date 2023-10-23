class PhoneNumber:
    def __init__(self, number, fio) -> None:
        self.number = number
        self.fio = fio
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, number):
        self.__number = number
        
    @property
    def fio(self):
        return self.__fio
    
    @fio.setter
    def fio(self, fio):
        self.__fio = fio

class PhoneBook:
    def __init__(self) -> None:
        self.__phones = list()
        
    def add_phone(self, phone):
        """добавление нового номера телефона (в список)"""
        self.__phones.append(phone)
        
    def remove_phone(self, indx):
        """удаление номера телефона по индексу списка"""
        self.__phones.pop(indx)
        
    def get_phone_list(self):
        """получение списка из объектов всех телефонных номеров"""
        return self.__phones
    
p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list() #?
