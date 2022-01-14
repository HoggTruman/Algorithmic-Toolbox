def get_change(m):
    coins = 0
    while m >= 10:
        m -= 10
        coins += 1
    if m >= 5:
        m -= 5
        coins += 1
    if m != 0:
        coins += m
    return coins


m = int(input())
print(get_change(m))
