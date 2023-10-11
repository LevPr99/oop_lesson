a = [{2, 4, 8, 10, 13, 14},
     {4, 5, 7, 8, 12, 15},
     {1, 2, 3, 6, 11, 13},
     {3, 5, 6, 9, 10, 15},
     {1, 7, 9, 11, 12, 14}]

res = set()
for i in a:
        res.update(i)
print(res := sorted(list(res)))