turns=int(input("Sláðu inn fjölda talna sem þú vilt slá inn: "))
counter=0
for i in range(1,turns+1):
    tala=int(input("Sláðu inn tölu: "))
    if tala < 0:
        counter +=1
print("Fjöldi neikvæðra talna er: ",counter)


