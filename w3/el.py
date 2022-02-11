l=['palindrome', 'madamimadam', '', 'foo', 'eyes']
o=[]
w='avish'

def check(a):
        word=a[::-1]
        if word==a or a=='':
            return True
        else:
            return False

for i in l:
    print(check(i))