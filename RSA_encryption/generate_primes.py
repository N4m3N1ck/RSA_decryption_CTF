import random
from math import gcd

length = int(input("Enter the desired length of the number: "))
tests_m = int(input("Enter the amount of miller-rabin tests (Increase the amount for higher chance of the number being prime): "))


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


def prime_test_slow(num):
    if n % 2 == 0 or n <= 1:
        return False
    if n <= 3:
        return True
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
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
while not (fermat_test(n) and miller_rabin_test(n, tests_m)):
    n = generate_random_number_of_length(length)
print(f"Very likely to be prime: {n}")
# print(prime_test_slow(n))
