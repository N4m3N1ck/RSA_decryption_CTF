p = int(input("p: "))
q = int(input("q: "))
e = int(input("e: "))
n = p * q
phi = (p - 1) * (q - 1)
i = 0

if (p - 1) % e == 0 or (q - 1) % e == 0:
    print("Please pick two other prime numbers: e is not coprime")
else:
    # (d*e) mod phi = 1
    # d*e = k*phi + 1
    # d = (k*phi+1)/e
    # We need to pick the right value for k so that d is an integer
    k = 1
    while (k * phi + 1) % e != 0:
        k += 1
    d = (k * phi + 1) // e
    print("n: ", n)
    print("e:", e)
    print("d: ", d)
