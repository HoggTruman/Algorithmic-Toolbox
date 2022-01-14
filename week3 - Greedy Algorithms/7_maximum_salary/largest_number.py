# Uses python3
import sys


def greaterequal(num, max_num):
    for i in range(max(len(max_num)+1, len(num))+1):
        if num[i % len(num)] > max_num[i % len(max_num)]: # better than
            return True
        if num[i % len(num)] < max_num[i % len(max_num)]: # worse than
            return False
    return True                                     # same as


def largest_number(a):
    a.sort(key=int, reverse=True)
    sol = ""
    while a:
        max_num = "0"
        for num in a:
            if greaterequal(num, max_num):
                max_num = num
        sol += max_num
        a.remove(max_num)
    return sol


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
