# Uses python3
import sys

def optimal_summands(n):
    summands = []
    current_prize=0
    while n > 0:
        current_prize+=1
        if n - 2*current_prize - 1 < 0:
            summands.append(n)
            n = 0
        else:
            summands.append(current_prize)
            n -= current_prize

        #print("remaining:",n)

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
