print('Welcome to car rentals!')
a=input('Would you like to continue (y/n)? ')
while a=='y':
    code=input('Customer code (b or d): ')
    if code == 'b':
        days=input('Number of days: ')
        odo_start=input('Odometer reading at the start: ')
        odo_end=input('Odometer reading at the end: ')
        miles=int(odo_end)-int(odo_start)
        print('Miles driven:', miles)
        amount=round(40*(int(days))+0.25*int(miles),1) 
        print('Amount due:', amount)
    else:
        days=input('Number of days: ')
        odo_start=input('Odometer reading at the start: ')
        odo_end=input('Odometer reading at the end: ')
        miles=int(odo_end)-int(odo_start)
        print('Miles driven:', miles)
        if miles>int(days)*100:
            amount=round(60*(int(days))+0.25*(int(miles)-int(100*int(days))),1)
            print('Amount due:', amount)
        else:
            amount=round(60*(int(days)),1)
            print('Amount due:', amount)
    a=input('Would you like to continue (y/n)? ')
# 44444
