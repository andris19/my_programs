low=int(input("Sláðu inn lægri töluna: "))
h=int(input("Sláðu inn hærri töluna: "))
if h <= low:
    low=int(input("Sláðu inn lægri töluna: "))
    h=int(input("Sláðu inn hærri töluna: "))
else:
    counter=low
    for i in range(low,h+1):
        print(counter)
        counter +=1



      



