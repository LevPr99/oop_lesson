class Handler:
    
    def __init__(self, methods=('GET', )):
        self.methods = methods
    
    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'
    
    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'
    
    def __call__(self, func):
        def wrapper(request: dict):
            m = request.get('method', 'GET')
            if m in self.methods:
                method = m.lower()
                return self.__getattribute__(method)(func, request)
        return wrapper
        

@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"

print(contact({}))