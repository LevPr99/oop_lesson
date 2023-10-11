def break_camelCase(line):
    i = 0
    len_l = len(line)
    while i < len_l:
        if ord(line[i]) < 97:
            tmp_l = line[:i]
            tmp_l += ' ' + line[i:]
            line = tmp_l
            i += 2
        else:
            i += 1
        len_l = len(line)
    return line
    

t = list(map(str, range(10))) #?
''.join(t) #?
ord('a') #?
break_camelCase('ABhelloWorldH') #?