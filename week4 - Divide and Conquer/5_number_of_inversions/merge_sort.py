def merge(b, c):
    new_a = [0]*(len(b)+len(c))
    i = 0
    j = 0
    k = 0
    max_b_index = len(b) - 1
    max_c_index = len(c) - 1
    while i <= max_b_index and j <= max_c_index:
        if b[i] > c[j]:
            new_a[k] = c[j]
            j += 1
            k += 1
        else:
            new_a[k] = b[i]
            i += 1
            k += 1
    if i > max_b_index:
        for element in c[j:]:
            new_a[k] = element
            k += 1
    else:
        for element in b[i:]:
            new_a[k:] = b[i:]
            k += 1
    return new_a


def merge_sort(a):
    if len(a) == 1:
        return a
    piv = len(a) // 2
    b = merge_sort(a[:piv])
    c = merge_sort(a[piv:])
    new_a = merge(b, c)
    return new_a


print(merge_sort([9,2,5,7,1,3,8,0,4,6]))

