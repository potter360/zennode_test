m1=10.00
m2=50.00
li=[12,15,28,33,46]
n=float(input("enter the number:"))
if(n<m1 or n>m2):
    print("Invalid number")
elif n>=m1 and n<=m2:
    for i in range(len(li)):
        if(n==li[i]):
            n+=1
    print("number=",+n)
else:print("number=",+n)    
