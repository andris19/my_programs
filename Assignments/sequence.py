n = int(input("Enter the length of the sequence: "))
tala1 = 1
tala2 = 2
tala3 = 3
print(tala1)
print(tala2)
print(tala3)

for i in range(1,n-2):
    summa=tala1+tala2+tala3
    tala1 = tala2
    tala2 = tala3
    tala3 = summa
    print(summa)
    
    
