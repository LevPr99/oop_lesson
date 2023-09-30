class Car:
    
    def __init__(self):
        self.model = None
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        if isinstance(model, str) and len(model) in range(2, 101):
            self.__model = model
        
    
car = Car()
car.model = 'TototototoTototototoTototototoTototototoTototototoTototototoTototototoTototototoTototototoTototototof'
car.model = 'BMW'

print(car.model)