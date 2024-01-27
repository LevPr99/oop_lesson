class Handler:
    
    def __init__(self, methods):
        self.methods = methods
    
    def get(self, func, request, *args, **kwargs):
        return f'{self.get.__name__.upper()}: {func(args)}'
    
    def post(self, func, request, *args, **kwargs):
        return f'{self.get.__name__.upper()}: {func(args)}'
        
    def __call__(self, func):
        def wrapper(*args):
            return func()
        return wrapper
        

@Handler
def contact(request):
    return "Сергей Балакирев"

print(contact({"method": "GET", "url": "contact.html"}))