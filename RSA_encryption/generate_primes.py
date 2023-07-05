import random
length = int(input("Enter the desired length of the number: "))
tests = int(input("Enter the amount of fermat's tests (recommended 10): "))


def generate_random_number_of_length(n):
    s = ""
    s += str(random.randint(1, 9))
    for i in range(n-1):
        s += str(random.randint(0, 9))
    return int(s)


def fermat_test(num,count):
    for i in range(count):
        a = random.randint(2, num-1)
        if pow(a, num-1, num) != 1:
            return False
    return True


def prime_test_slow(num):
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True


n = generate_random_number_of_length(length)
while not fermat_test(n,tests):
    n = generate_random_number_of_length(length)
print(f"Very likely to be prime: {n}")
# print(prime_test_slow(n))