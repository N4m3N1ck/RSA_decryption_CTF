import random
from math import gcd


length = int(input("Enter the desired length of the number (p): "))
coprime = int(input("Enter the number (e) p-1 should be coprime with (Enter 1 to ignore): "))
tests_m = int(input("Enter the amount of miller-rabin tests: "))


def generate_random_number_of_length(n):
    s = ""
    s += str(random.randint(1, 9))
    for i in range(n - 1):
        s += str(random.randint(0, 9))
    return int(s)


def fermat_test(num):
    if n % 2 == 0 or n <= 1:
        return False
    if n <= 3:
        return True
    a = random.randint(2, num - 1)
    if pow(a, num - 1, num) != 1:
        return False
    return True


def miller_rabin_test(num, tests):
    if num % 2 == 0 or num <= 1:
        return False
    if num <= 3:
        return True

    s = 0
    d = num - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for i in range(tests):
        a = random.randint(2, num - 2)
        x = pow(a, d, num)
        for j in range(s):
            y = pow(x, 2, num)
            if y == 1 and x != 1 and x != num - 1:
                return False
            x = y
        if y != 1:
            return False
    return True


n = generate_random_number_of_length(length)
while not (fermat_test(n) and miller_rabin_test(n, tests_m) and gcd(coprime, n-1) == 1):
    n = generate_random_number_of_length(length)
print(f"Very likely to be prime: {n}")
