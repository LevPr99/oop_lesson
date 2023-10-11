lst = list(range(-100, 100))

def bin_f(lst : list, find_val):
    low = 0
    high = len(lst) - 1
    mid = high // 2
    i = 0
    while low <= high:
        mid = (high + low) // 2
        print(i := i + 1)
        tmp = lst[mid]
        if tmp == find_val:
            return mid
        
        if tmp > find_val:
            high = mid - 1
        else:
            low = mid + 1
    return None

f_ = -22
print(bin_f(lst, f_)) #?

lst.index(f_) #?