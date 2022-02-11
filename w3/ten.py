l="() (( ( )() ( )) ) ( ())"
d=l.replace(" ","")
print(d)
c1=0
l1=""
l2=[]

for i in d:
    if i=="(":
        c1+=1
        l1=l1+i
    elif i==")":
        c1-=1
        l1=l1+i

    if c1==0:
        l2.append(l1)
        l1=""

print(l2)
