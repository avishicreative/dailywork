l=[1, 2, 3, 4,1, 2, 3,4,5,6,7,8]
l1=[]
count=0

for i in l:
    if (i)>20:
        print("true")
        break
    l1.append(i)
    count=count+1
    if count==4:
        s1=set(l1)
        if len(s1)<4:
            print("false")
            break

        if l1*3==l or l1*4==l:
            print('true')
        else:
            print("false")

