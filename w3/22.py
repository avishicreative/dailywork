string='PytHon ExerciSEs'
sum=0
for i in string:
    if i.isupper() and i.isalpha():
        sum=sum+ord(i)
print(sum)