a0 = int(input("Input a positive int: "))# Do not change this line
counter = 0
while a0>1:
    if counter%2 == 0:
        a0 = a0/2
        counter += 1
        print(a0)
    else:
        a0 = 3*a0+1
        counter +=1
        print(a0)
