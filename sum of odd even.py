n=int(input("enter a number"))
eventotal=0
oddtotal=0
for i in range(1,n+1):
    if(i%2==0):
        eventotal=eventotal+i
    else:
        oddtotal=oddtotal+i
print("even totel=",eventotal,"odd totel=",oddtotal)