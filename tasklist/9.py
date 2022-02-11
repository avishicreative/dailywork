t1=('Tom',19,80)
t2=('John',20,90)
t3=('Jony',17,91)
t4=('Jony',17,93)
t5=('Json',21,85)

l=[t1,t2,t3,t4,t5]
l1=[]
l2=[]
l3=[]

for i in l:
    l1.append(i[0])
    l2.append(i[1])
    l3.append(i[2])
l1.sort()
#l2.sort()
#l3.sort()

for i in zip(l1,l2,l3):
    print(i)