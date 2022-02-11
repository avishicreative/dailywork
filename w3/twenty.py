l=[ 5,4,3,2,1]

def check(l):
    c1 = 1
    c2 = 1
    for i in range(len(l)):
        if l[i-1]>l[i]:
            c1=c1+1

        elif l[i-1]<l[i]:
            c2=c2+1

    if c2==len(l):
        print("inc")

    elif c1==len(l):
        print("dec")
    else:
        print("not")

check(l)