class HandlerGET:
    
    def __init__(self, func):
        self.func = func
    
    def get(self, func, request, *args, **kwargs):
        if 'method' not in request or request['method'] == 'GET':
            return f'GET: {func(args)}'
        return None
        
    def __call__(self, *args):
        return self.get(self.func, request=args[0])

  
@HandlerGET
def contact(request):
    return "Сергей Балакирев"

# print(contact({"method": "GET", "url": "contact.html"}))