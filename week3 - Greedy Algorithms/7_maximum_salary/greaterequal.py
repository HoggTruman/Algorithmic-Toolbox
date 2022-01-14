def greaterequal(num, max_num):
    for i in range(max(len(max_num)+1, len(num))+1):       # IS THIS RIGHT???  #assumes the new number being tested has less digits??
        if num[i % len(num)] > max_num[i % len(max_num)]: # better than
            return True
        if num[i % len(num)] < max_num[i % len(max_num)]: # worse than
            return False
    print("equal")
    return True


input = input().split()
print(greaterequal(input[0], input[1]))
