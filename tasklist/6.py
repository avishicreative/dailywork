sent=input("enter sentence")
c1=0
c2=0
l=len(sent)
for s in sent:
    if s.isupper():
        c1=c1+1
    elif s.islower():
        c2=c2+1

print(c1)
print(c2)
