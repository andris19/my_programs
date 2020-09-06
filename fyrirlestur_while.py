num=int(input("input a number: "))
counter = 0

while counter < num: #á meðan counterinn er minni en num
    print(counter, end=' ') #end=' ' prentar í sömu línu
    counter += 1 #bæti einum við counterinn í hverri umferð
    if counter == 5: #ef við viljum einhverra hluta vegna hætta þegar counterin er 5
        break
else:
    print('done')
    

