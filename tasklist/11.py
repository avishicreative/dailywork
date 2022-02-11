str=input("enter comma seperated numbers:")
l=str.split(",")
o=[]
for i in l:
   o.append(int(i))

op=[i*i for i in o if i%2!=0]
print(op)