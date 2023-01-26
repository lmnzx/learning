# naive solution
# time complexity: O(max(a, b))
def slowlcm(a, b):
    res = max(a, b)
    while (res % a != 0 or res % b != 0):
        res += 1
    return res


def fastgcd(a, b):
    if (b == 0):
        return a
    return fastgcd(b, a % b)

# fast solution
# time complexity: O(log min(a, b))
# base on euclidean algorithm
# lcm(a, b) = (a * b) / gcd(a, b)


def fastlcm(a, b):
    return (a * b) // fastgcd(a, b)


print(slowlcm(4, 6))
print(fastlcm(4, 6))
