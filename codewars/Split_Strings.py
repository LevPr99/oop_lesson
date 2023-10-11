def solution(s):
    i = 0
    res = list()
    len_str = len(s)
    while i < len_str:
        if len_str % 2 == 0:
            res.append(s[i:i + 2])
        else:
            if i + 1 >= len_str:
                res.append(s[i:] + '_')
            else:
                res.append(s[i:i + 2])
        i += 2
    return res

solution('asdfgghhasddf') #?