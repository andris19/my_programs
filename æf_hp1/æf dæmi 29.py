turns = int(input("Hversu margar tölur viltu slá inn? "))
nei = 0
ja = 0
sum_n=0
sum_j=0
for i in range(1,turns+1):
    num=int(input("Sláðu inn tölu: "))
    if num < 0:
        nei +=1
        sum_n=sum_n+num
    elif num >= 0:
        ja +=1
        sum_j=sum_j+num
print("neikvæðar tölur eru: ",nei)
print("Summa neikvæðra er: ",sum_n)
print("Jákvæðar tölur eru: ",ja)
print("Summa jákvæðra er: ",sum_j)