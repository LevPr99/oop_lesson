def simple_find(text, f):
    i = 0
    j = 0
    while i < len(text):
        while j < len(f):
            if text[i + j] != f[j]:
                j = 0
                break
            else:
                j += 1
        else:
            return i
        i += 1
    return -1

t = 'lililos lililas'
f = 'il'
print(simple_find(t, f))

