class Dec:
    
    def __init__(self, func):
        print('INIT start')
        self.func = func
        print('INIT end')
        
    def __call__(self, *args):
        print('CALL start')
        self.func(*args)
        print('CALL DO SOMETHING AFTER self.func')
        
@Dec
def test(a1, a2):
    print('TEST')
    print(f'a1: {a1} a2: {a2}')

print('Prepare to TEST')
test('say', 'hello')
print('After TEST')


#  INIT start
#  INIT end
#  Prepare to TEST
#  CALL start
#  TEST
#  a1: say a2: hello
#  CALL DO SOMETHING AFTER self.func
#  After TEST