l=['0001', '1011']
for n in range(len(l)-1):
    n1=int(l[n])
    n2=int(l[n+1])
    ans=n1^n2
print("0b",ans)