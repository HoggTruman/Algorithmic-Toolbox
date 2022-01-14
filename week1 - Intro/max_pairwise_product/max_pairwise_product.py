def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_nums = [0, 0]
    max_nums[0] = max(numbers)
    max_index = numbers.index(max_nums[0])

    for i in range(n):
        if i != max_index and numbers[i] > max_nums[1]:
            max_nums[1] = numbers[i]

    return max_nums[0] * max_nums[1]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
