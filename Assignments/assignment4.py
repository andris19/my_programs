max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))
counter=1
for i in range(1,max_days+1):
    dollars=2**(i-1)
    print(dollars)
    if dollars>=target:
        days_when_amount_acquired=i
        break
    else: 
        days_when_amount_acquired=0


print('Days needed:',days_when_amount_acquired)
