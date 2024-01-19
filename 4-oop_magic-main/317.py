# from dataclasses import dataclass, field


class ValidateString:
    
    def __set_name__(self, owner, name):
        self.name = name
        
    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.name]
    
    def __set__(self, obj, value):
        if isinstance(value, str):
            obj.__dict__[self.name] = value


class SmartPhone:
    
    model = ValidateString()
    
    def __init__(self, model):
        self.model = model
        self.apps = list()
        
    def add_app(self, app):
        if not any((lambda app, apps: [type(app) == type(x) for x in apps])(app, self.apps)):
            self.apps.append(app)
    
    def remove_app(self, app):
        if app in self.apps: 
            self.apps.remove(app)


class AppVK:
    
    def __init__(self, name="ВКонтакте") -> None:
        self.name = "ВКонтакте"

class AppYouTube:
    
    def __init__(self, memory_max, name="YouTube") -> None:
        self.name = name
        self.memory_max = memory_max

class AppPhone:
    
    def __init__(self, phone_list: dict, name = "Phone") -> None:
        self.name = name
        self.phone_list = phone_list


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)