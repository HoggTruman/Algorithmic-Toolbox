
def fibonacci_partial_sum_naive(start, finish):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


input = input()
start, finish = map(int, input.split())
print(fibonacci_partial_sum_naive(start, finish))
