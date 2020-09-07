fab =input('Input f|a|b (fibonacci, abundant or both): ')
if fab=='f':  # Ef valið er fibonacci 
    fib_length = int(input('Input the length of the sequence: ')) 
    print('Fibonacci Sequence:')
    print('-------------------')
    tala1=0
    tala2=1
    print(tala1)
    print(tala2)
    for i in range(1,fib_length-1): 
        summa=tala1+tala2
        tala1 = tala2 #uppfæri tölurnar, tala 1 í summunni verður gamla tala 2
        tala2 = summa # tala 2 verður summan af gömlu tölum 1 og 2
        print(summa)
elif fab=='a':  # ef valið er abundant numbers
    max_num=int(input('Input the max number to check: '))
    print('Abundant numbers:')
    print('-----------------')
    for i in range(1,max_num+1):
        summa_deilna=0
        for j in range(1,i):
            a=i%j # tjékka á afgangum af i deilt með j fyrir öll j frá 1 uppí i
            if a==0: # ef enginn afganur þá bæti ég j við summu deilna
                summa_deilna +=j
                if summa_deilna > i: 
                    print(i)
                    break
elif fab == 'b': # ef bæði eru valin
    fib_length = int(input('Input the length of the sequence: '))
    print('Fibonacci Sequence:')
    print('-------------------')
    tala1=0
    tala2=1
    print(tala1)
    print(tala2)
    for i in range(1,fib_length-1):
        summa=tala1+tala2
        tala1 = tala2
        tala2 = summa
        print(summa)

    max_num=int(input('Input the max number to check: '))
    print('Abundant numbers:')
    print('-----------------')
    for i in range(1,max_num+1):
        summa_deilna=0
        for j in range(1,i):
            a=i%j
            if a==0:
                summa_deilna +=j
                if summa_deilna > i:
                    print(i)
                    break
                
        
            
