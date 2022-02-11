eq='a+aa+aaa+aaaa'
num=input('Enter any number:')

sum=""
sum1=0
for i in range(4):
    sum=sum+num
    s1=int(sum)
    sum1=sum1+s1
print(sum1)