n = int(input("Input a natural number: "))
counter = 2
while counter < n:
    if n % counter == 0:
        print("not prime")
        break
        counter += 1
    else:
        print("prime")
        break