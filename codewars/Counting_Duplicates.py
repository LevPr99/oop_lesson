def duplicate_count(text):
    tmp = dict()
    c = 0
    for i in text.upper():
        if tmp.get(i) is not None:
            tmp[i] += 1
        else:
            tmp[i] = 1
    for i in list(tmp.values()):
        if i > 1:
            c += 1
    return c
        
text = 'aaff1123124234'
duplicate_count(text) #?