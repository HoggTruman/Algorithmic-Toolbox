import math as m


def majority_element(keys):
    keys.sort()
    criteria = m.ceil((len(keys)+1)/2)
    if len(keys) % 2 == 1:
        focus_index = int((len(keys) - 1) / 2)
        focus_element = keys[focus_index]
        count = 0
        for i in range(0, len(keys)):
            if keys[i] == focus_element:
                count += 1
            if count == criteria:
                return 1
    else:
        for val in [0, 1]:
            focus_index = int(len(keys)/ 2) - val
            focus_element = keys[focus_index]
            count = 0
            for i in range(0, len(keys)):
                if keys[i] == focus_element:
                    count += 1
                if count == criteria:
                    return 1

    return 0


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    # num_queries = int(input())
    # input_queries = list(map(int, input().split()))
    # assert len(input_queries) == num_queries

    print(majority_element(input_keys))


#NOTES
#if odd number of elements only the middle element can be a majority
#if even, either of the middle elements could be a majority