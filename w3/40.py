a='pYTHaN'
b=''
for i in a:
    if i in ['a','e','i','o','u','A','E','I','O','U']:

        b=b+chr(ord(i)+2).swapcase()
    else:
        b = b + i .swapcase()


print(b)
