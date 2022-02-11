l=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def sum(n):
    n1=str(n)
    sum=0
    for n2 in n1:
        n3=int(n2)
        sum=sum+n3
    return sum

d1={}
for i in l:
    d1[i]=sum(i)
print(d1.values())