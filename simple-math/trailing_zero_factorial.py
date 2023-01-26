# naive solution
# time complexity: O(n)
def slow(n):
    fact = 1
    for i in range(2, n+1):
        fact = fact * i
    res = 0
    while (fact % 10 == 0):
        res += 1
        fact = fact // 10
    print(res)

# fast solution
# time complexity: O(log n)


def fast(n):
    res = 0
    while (n > 0):
        res += n // 5
        n = n // 5
    print(res)


slow(251)
fast(251)
