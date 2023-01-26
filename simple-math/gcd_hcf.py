# naive gcd solution
# time complexity: O(min(a, b))
def slowgcd(a, b):
    res = min(a, b)
    while (res > 0):
        if (a % res == 0 and b % res == 0):
            break
        res -= 1
    print(res)

# fast gcd solution
# euclidean algorithm
# time complexity: O(log min(a, b))


def fastgcd(a, b):
    if (b == 0):
        return a
    return fastgcd(b, a % b)


slowgcd(10, 15)
print(fastgcd(10, 15))
