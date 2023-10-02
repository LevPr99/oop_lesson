class AppStore:
    
    def __init__(self):
        self.app_list = dict()
        
    def add_application(self, app):
        self.app_list[app.id] = app
        
    def remove_application(self, app):
        self.app_list.pop(app.id, f'Not found app {app.name}')
        
    def block_application(self, app):
        self.app_list[app.id].blocked = True
        
    def total_apps(self):
        return len(self.app_list)
    
class Application:
    
    id = 0
    
    def __new__(cls, *args, **kwargs):
        cls.id += 1
        return super().__new__(cls)
    
    def __init__(self, name):
        self.id = self.id
        self.name = name
        self.blocked = False

store = AppStore()
app_youtube = Application("Youtube")
assert app_youtube.blocked == False, "начальное значение blocked должно быть равно False"

store.add_application(app_youtube)
store.block_application(app_youtube)

assert app_youtube.name == "Youtube" and app_youtube.blocked == True, "неверные значения локальных атрибутов объекта класса Application"

app_stepik = Application("Stepik")
store.add_application(app_stepik)


assert store.total_apps() == 2, f"неверное число приложений в магазине {store.total_apps()}"

store.remove_application(app_youtube)
assert store.total_apps() == 1, "неверное число приложений в магазине, некорректно работает метод remove_application"