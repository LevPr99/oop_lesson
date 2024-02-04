class Model:
    
    def __init__(self):
        self.model = dict()
    
    def query(self, **kwargs):
        self.model = kwargs

    def __str__(self):
        res = 'Model'
        if len(self.model):
            res += ': '
            for k, v in self.model.items():
                res += f'{k}={v}, '
            res = res[:-2]
            # return f"Model: {} = {}"
        return res
    
m = Model()
m.query(a=1, b=2, c=3)
print(m)