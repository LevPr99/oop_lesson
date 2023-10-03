import re
from random import Random
from string import ascii_letters, digits

class EmailValidator:
    
    chars_lst = ascii_letters + digits + '_'
    
    
    def __new__(cls):
        return None
    
    @classmethod
    def get_random_email(cls):
        """латинские буквы, цифры, символ подчеркивания и точка"""
        len_before = Random().randint(1, 101)
        len_after = Random().randint(1, 47)
        domen = Random().randint(1, 4)
        email = ''
        for _ in range(len_before):
            email += Random().choice(cls.chars_lst)
        email += '@'
        for _ in range(len_after):
            email += Random().choice(cls.chars_lst)
        email += '.'
        for _ in range(domen):
            email += Random().choice(cls.chars_lst)
        return email
    
    @classmethod
    def check_email(cls, email):
        return True if re.match(r'[a-zA-Z0-9_]{1,100}\@[a-zA-Z0-9_]{1,50}\.{1,4}', email) is not None else False
    
    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)
    
print(EmailValidator.get_random_email())
print(EmailValidator.check_email("sc_lib@list.ru"))
print(EmailValidator.check_email("sc_lib@list_ru"))
print(EmailValidator.check_email("2FbmUQm1f5TKjRCWSiN2vFSq7q9yvcCbW_ozmcsm10RWh96ZNL@8Q7dzszOBneylMTdKbWpRq2DPowulvkrfMaAxNQwk.o"))

