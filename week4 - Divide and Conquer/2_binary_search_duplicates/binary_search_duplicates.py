import math as m


def binary_search_duplicates(sequence, query):
    low = 0
    high = len(sequence) - 1

    while low <= high:
        pivot = m.floor((low+high)/2)
        pivotval = sequence[pivot]
        if pivotval == query:
            if pivot != 0 and sequence[pivot-1] == pivotval:
                high = pivot - 1
            else:
                return pivot
        elif pivotval < query:
            low = pivot + 1
        else:
            high = pivot - 1
    return -1



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_duplicates(input_keys, q), end=' ')


#want to find the first instance of a duplicate