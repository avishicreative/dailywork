l=[('do',('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]

l1=l[0][0]
l2=list(l[0])
l3=[]
print(l2)

for i in l2[1]:
    w=i[:2]
    if w==l1:
        l3.append(i)
print(l3)
