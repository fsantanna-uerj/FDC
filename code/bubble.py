L = [ 6, 5, 3, 1, 8, 7, 2, 4 ]
print('>>>', L)

i = len(L)-1
while i > 0:
    j = 0
    print'---'
    while j < i:
        v1 = L[j]
        v2 = L[j+1]
        if v1 > v2:
            L[j]   = v2
            L[j+1] = v1
        print(L)
        j += 1
    i -= 1

print('<<<', L)
