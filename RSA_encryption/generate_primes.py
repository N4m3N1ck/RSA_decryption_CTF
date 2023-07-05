import random
length = int(input("Enter desired number length: "))
count = int(input("Enter amount of numbers you want to generate: "))


def generate_random_number_of_length(n):
    s = ""
    s += str(random.randint(1, 9))
    for i in range(n-1):
        s += str(random.randint(0, 9))
    return int(s)

