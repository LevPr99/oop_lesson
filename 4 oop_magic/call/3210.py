class RenderDigit:
    
    def __call__(self, digit):
        out = ''
        try:
            out = int(digit)
        except ValueError:
            out = None
        return out


class InputValues:
    
    def __init__(self, render):
        self.__render = render

    def __call__(self, func):
        def wrapper(*args):
            res = list()
            args = input()
            for i in args.split():
                res.append(self.__render(i))
            return res
        return wrapper
    
input_dg = InputValues(RenderDigit())(input)

res = input_dg()