p = int(input("p: "))
q = int(input("q: "))
n = p * q
phi = (p - 1) * (q - 1)

fermat_numbers = [65537, 257, 17, 5]
e = 65537
i = 0
while ((p - 1) % e == 0 or (q - 1) % e == 0) or e >= phi:
    i += 1
    e = fermat_numbers[i]
if (p-1)%e==0 or (q-1)%e==0:
    print("Please pick two other prime numbers")
else:
    # (d*e) mod phi = 1
    # d*e = k*phi + 1
    # d = (k*phi+1)/e
    # We need to pick the right value for k so that d is an integer
    k=1
    while (k*phi+1)%e!=0:
        k+=1
    d = (k*phi+1)//e
    print("n: ",n)
    print("e:", e)
    print("d: ",d)

