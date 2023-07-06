from math import gcd


# Converts int message into text


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


def calculate_private_key_n_p_q_e(n, p, q, e):
    phi = (p - 1) * (q - 1)
    if gcd(e, phi) != 1:
        raise ValueError("e and phi(n) are not coprime. Choose a different value for e.")
    d = pow(e, -1, phi)
    return d


# Example usage
n = int(input("n: "))
p = int(input("p: "))
q = int(input("q: "))
e = int(input("e: "))
c = int(input("c: "))

private_key = calculate_private_key_n_p_q_e(n, p, q, e)
print("Private Key (d):", private_key)
m = pow(c, private_key, n)
print("Message m: ", m)
print("Result (base 256): ", to_base_256(m))
