l=[('do',('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]

l1=l[0][0]
l2=list(l[0])
l3=[]
print(l2)


for i in l2[1]:
    if l1 in i:
        l3.append(i)
print(l3)
