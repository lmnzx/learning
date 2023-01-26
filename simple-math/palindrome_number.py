# trivial solution
def sol(n):
    rev = 0
    temp = n
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return temp == rev


print(sol(12321))
