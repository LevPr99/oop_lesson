class Handler:
    
    def __init__(self, func):
        self.func = func
    
    def get(self, func, request, *args, **kwargs):
        if 'method' not in request or request['method'] == {self.get.__name__.upper()}:
            return f'{self.get.__name__.upper()}: {func(args)}'
        return None
    
    def post(self, func, request, *args, **kwargs):
        if 'method' not in request or request['method'] == {self.get.__name__.upper()}:
            return f'{self.get.__name__.upper()}: {func(args)}'
        return None
        
    def __call__(self, *args):
        def wrapper(func):
            return func(args[0])
        return wrapper(self.func)
        
  
@Handler
def contact(request):
    return "Сергей Балакирев"

print(contact({"method": "GET", "url": "contact.html"}))