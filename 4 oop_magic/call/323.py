from random import randint

# здесь объявляйте класс RandomPassword
class RandomPassword:
    
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self):
        password = randint(self.min_length, self.max_length)