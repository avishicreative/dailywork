
l1=[]
sum=0
for i in range(5):
    tra=input("Enter transection")
    if tra[0]=='d':
        s=int(tra[1:])
        sum=sum-s
    elif tra[0]=='c':
        s=int(tra[1:])
        sum=sum+s
    else:
        continue
print(sum)