a = int(input("Sláðu inn tölu a: "))
b = int(input("Sláðu inn tölu b: "))
val = int(input("sláðu inn tölu 1,2 eða 3: "))
if val == 1:
    result = a+b
    print(result)
elif val == 2:
    result = a-b
    print(result)
elif val == 3:
    result = a*b
    print(result)
else:
    print("invalid input")