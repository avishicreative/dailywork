def check(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    return max(l)

print(check(97))

