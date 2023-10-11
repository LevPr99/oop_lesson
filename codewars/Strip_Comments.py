import re

def solution(user_string: str, args):
    i = 0
    j = 0
    stop_symbol = '\n'
    res = list()
    while i < len(user_string):
        if user_string[i] in args:
            stop = user_string.find(stop_symbol, i)
            tmp = re.sub(r'[$] *', '', user_string[j:i]) #?
            res.append(tmp)
            j = stop
        i += 1
    res = ''.join(res)
    return res

print(solution('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])) #?