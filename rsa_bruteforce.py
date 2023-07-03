def x_root(n,x):
    left = 0
    right = n
    while left <= right:
        mid = (right + left) // 2
        if mid ** x <= n < (mid + 1) ** x:
            return mid
        elif mid ** x > n:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def to_base_256(i):
    encoded_integer = i

    # Convert the integer to base 256
    base256_digits = []
    while encoded_integer > 0:
        encoded_integer, remainder = divmod(encoded_integer, 256)
        base256_digits.append(remainder)

    # Reverse the digits to get the correct order
    base256_digits.reverse()

    # Convert the digits to bytes
    encoded_bytes = bytes(base256_digits)

    return encoded_bytes


n = int(input("n: "))
c = int(input("c: "))
e = int(input("e: "))
rng_0 = int(input("loop range start: "))
rng_1 = int(input("loop range finish: "))
target = input("target string: ")
# m**e%n=c
# m**e = i*c+n
# m = (i*c+n)**(1/3)
for i in range(rng_0,rng_1):
    m = x_root(i * n + c,e)
    if m % 1 == 0:
        s = str(to_base_256(m))
        print(f"number: {i}\nmessage: {m}\nstring: {s}")
        if target in s:
            break

