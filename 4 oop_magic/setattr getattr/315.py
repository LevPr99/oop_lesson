from abc import ABC, abstractmethod


class Validator(ABC):
    
    def __set_name__(self, owner, name):
        # self.private_name = '__' + name
        self.private_name = name
        # self.publick_name = name
    
    def __set__(self, obj, value):
        self.validate(value)
        obj.__dict__[self.private_name] = value
        
    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.private_name]
    
    @abstractmethod
    def validate(self, value):
        pass


class NumberValidator(Validator):
    
    def validate(self, value):
        if not isinstance(value, (int)):
            raise TypeError("Неверный тип присваиваемых данных.")
        if value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")


class StringValidator(Validator):
    
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")


class LessonItem:
    
    title = StringValidator()
    practices = NumberValidator()
    duration = NumberValidator()
    
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration
    

    def __getattribute__(self, name):
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        return False
    
    def __setattr__(self, name, value):
        # if name == 'title':
        #     if self.check_strings(value):
        #         super().__setattr__(name, value)
        #     else:
        #         raise TypeError("Неверный тип присваиваемых данных.")
        # elif name in ('practices', 'duration'):
        #     if self.check_numbers(value):
        #         super().__setattr__(name, value)
        #     else:
        #         raise TypeError("Неверный тип присваиваемых данных.")
        # else:
        super().__setattr__(name, value)
        
    def __delattr__(self, name):
        if name not in ('title', 'practices', 'duration'):
            super().__delattr__(name)
    
    # def check_strings(self, value):
    #     if isinstance(value, str):
    #         return True
    #     else:
    #         return False
        
    # def check_numbers(self, value, min_val=0):
    #     if isinstance(value, int):
    #         return value > min_val
    #     else:
    #         return False
            

class Module:
    
    name = StringValidator()
    
    def __init__(self, name):
        self.name = name
        self.lessons = list()
        
    def add_lesson(self, lesson):
        self.lessons.append(lesson)
    
    def remove_lesson(self, indx):
        if indx < len(self.lessons):
            self.lessons.pop(indx)


class Course:
     
    # name = StringValidator()
    
    def __init__(self, name):
        self.name = name
        self.modules = list()
         
    def add_module(self, module):
        self.modules.append(module)
    
    def remove_module(self, indx):
        if indx < len(self.modules):
            self.modules.pop(indx)
            

course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
s = LessonItem("Урок 3", 5, 800)
module_1.add_lesson(s)
print(s.__dict__)
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)