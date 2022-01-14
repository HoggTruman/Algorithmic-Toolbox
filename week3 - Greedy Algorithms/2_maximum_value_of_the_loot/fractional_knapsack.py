# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    valbyweight = [0]*n
    for i in range(n):
        valbyweight[i] = values[i]/weights[i]

    while capacity != 0 and valbyweight != []:
        max_value = max(valbyweight)
        max_index = valbyweight.index(max_value)
        value += min(values[max_index], capacity/weights[max_index] * values[max_index])
        capacity -= min(weights[max_index], capacity)
        del valbyweight[max_index]
        del weights[max_index]
        del values[max_index]

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
