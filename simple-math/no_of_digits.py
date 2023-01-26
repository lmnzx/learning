import math

# trivial solution


def slow(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

# optimised solution


def fast(n):
    return math.floor(math.log10(n)) + 1


# call the function
print(slow(123456789))
print(fast(123456789))
