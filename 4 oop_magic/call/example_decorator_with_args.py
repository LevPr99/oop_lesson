class Dec:
    
    def __init__(self, arg1, arg2, arg3):
        print('\n1. INIT start\nINIT create instance for class')
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        print('2. INIT end\n')
        
    def __call__(self, func):
        print('3. CALL start')
        def wrapper(*args):
            print('6. Wrapper start')
            print('Print func args: ', args)
            print('8. Wrapper end\n9. and return (call) test(*args)\n')
            return func(*args)
        print(self.arg1, self.arg2, self.arg3)  # Do something with self args
        print('4. CALL end\n')
        return wrapper

@Dec('Do', 'something', 'with self args')
def test(other_arg1, other_arg2):
    print('10. TEST start')
    print(f'other_arg1: {other_arg1}, other_arg2: {other_arg2}')
    print('11. TEST end\n')
    
print('5. Preparing to TEST')
test('call', 'test')

print('12. Other code actions')

#  1. INIT start
#  INIT create instance for class
#  2. INIT end
 
#  3. CALL start
#  Do something with self args
#  4. CALL end
 
#  5. Preparing to TEST
#  6. Wrapper start
#  Print func args:  ('call', 'test')
#  8. Wrapper end
#  9. and return (call) test(*args)
 
#  10. TEST start
#  other_arg1: call, other_arg2: test
#  11. TEST end
 
#  12. Other code actions