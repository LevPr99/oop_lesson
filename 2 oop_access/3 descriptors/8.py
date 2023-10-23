class ValidateString:
    
    def __init__(self, min_length, max_length) -> None:
        self.min_length = min_length
        self.max_length = max_length
    
    def __set_name__(self, owner, instance):
        self.validator = '__' + instance
    
    def __get__():
        pass
    
    def __set__():
        pass
    
    def validate(self, string):
        return isinstance(string, str) and (self.min_length <= len(string) <= self.max_length)


class StringValue:
    
    def __init__(self, valid_string) -> None:
        self.validator = valid_string


class RegisterForm:
    
    def __init__(self, login, password, email) -> None:
        self.login = StringValue()
        self.password = StringValue()
        self.email = StringValue()
    
    def get_fields(self):
        return [v for v in self.__dict__.values()]
    
    def show(self):
        print(f'<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>')
        
        

assert hasattr(ValidateString, 'validate'), "в классе ValidateString отсутствует метод validate"

r = RegisterForm('11111', '1111111', '11111111')
assert hasattr(r,'login') and hasattr(r, 'password') and hasattr(r, 'email'), "в классе RegisterForm должны быть дескрипторы login, password, email"

assert hasattr(RegisterForm, 'show'), "в классе RegisterForm отсутствует метод show"

StringValue.__doc__

frm = RegisterForm("123", "2345", "sc_lib@list.ru")
frm.get_fields() #?

frm.login = "root"
assert frm.login == "root", "дескриптор login вернул неверные данные"

v = ValidateString(5, 10)
assert v.validate("hello"), "метод validate вернул неверное значение"
assert v.validate("hell") == False, "метод validate вернул неверное значение"
assert v.validate("hello world!") == False, "метод validate вернул неверное значение"


class A:
    st = StringValue(validator=ValidateString(3, 10))


a = A()
a.st = "hello"

assert a.st == "hello", "дескриптор StringValue вернул неверное значение"
a.st = "d"
assert a.st == "hello", "дескриптор StringValue сохранил строку длиной меньше min_length"
a.st = "dапарпаропропропропр"
assert a.st == "hello", "дескриптор StringValue сохранил строку длиной больше max_length"
a.st = "dапарпароп"
assert a.st == "dапарпароп", "дескриптор StringValue сохранил строку длиной больше max_length"