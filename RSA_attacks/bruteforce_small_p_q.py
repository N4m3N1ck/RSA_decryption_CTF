n = int(input("Enter n: "))
p = 2
while True:
    if n%p == 0:
        print("p: "+ str(p),"q: " + str(n//p))
        break
    else:
        p+=1
