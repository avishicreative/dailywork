numl=input("enter numbers")
l=numl.split(",")
l=numl.replace(",","")
l=[int(i)*int(i) for i in l if int(i)%2!=0 ]

print(l)