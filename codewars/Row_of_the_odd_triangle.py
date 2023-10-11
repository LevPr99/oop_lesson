# 3: (1) (3 5) (7 9 11)

def odd_row(n):
    sum_n = sum(range(1, n + 1)) * 2
    res = set()
    for i in range(1, sum_n, 2):
        res.add(i)
    res = list(res)
    return res[-n:]
sum_n = sum(range(1, 4111 + 1)) * 2 #?

odd_row(4111)