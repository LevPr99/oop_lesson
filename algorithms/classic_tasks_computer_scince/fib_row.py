# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

# fib(n) = fib(n - 1) + fib(n - 2)

def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n - 1) + fib1(n - 2)

if __name__ == '__main__':
    print(fib1(6)) #?
    
# В рекурсивной функции базовый случай служит точкой остановки.
# В данном примере базовый случай - это n < 2



# Мемоизация

memo : dict = {0: 0, 1: 1}

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]

# При n = 5:
# если 5 не в memo, то memo[5] = fib3(4) + fib3(3) =>
# если 4 не в memo, то memo[4] = fib3(3) + fib3(2)  
#       &&  если 3 не в memo, то memo[3] = 1 + 1
#                           fib3(2) -> 1 т.к. 2 - 1 = 1 и 2 - 2 = 0 и эти значения есть в memo
#                           fib(1) -> 1 т.к. он есть в memo