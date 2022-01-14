# Uses python3
import sys


def merge(b, left, right, ave):
    print("left:", left, "right:", right, "ave:", ave)
    print(b)
    a1 = b[left:ave]
    print(a1)
    a2 = b[ave:right]
    print(a2)
    num_inversions = 0
    i = 0
    j = 0
    k = left
    max_a1_index = len(a1) - 1
    max_a2_index = len(a2) - 1
    while i <= max_a1_index and j <= max_a2_index:
        if a1[i] > a2[j]:
            num_inversions += 1
            b[k] = a2[j]
            j += 1
            k += 1
        else:
            b[k] = a1[i]
            i += 1
            k += 1
    if i > max_a1_index:
        for element in a2[j:]:
            b[k] = element
            k += 1
    else:
        for element in a1[i:]:
            b[k] = element
            k += 1
    print(b,"\n")
    return num_inversions



def mergesort_inversions(a, b, left, right):
    num_inversions = 0
    if right <= left:
        b[left] = a[left]
        return num_inversions
    ave = (left + right + 1) // 2
    num_inversions += mergesort_inversions(a, b, left, ave)
    num_inversions += mergesort_inversions(a, b, ave+1, right)
    num_inversions += merge(b, left, right, ave)
    return num_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(mergesort_inversions(a, b, 0, len(a)-1))
    print(b)

test1 = [9,2,5,7,1,3,8,0,4,6]
b = len(test1)*[0]
mergesort_inversions(test1,b,0,len(test1)-1)
