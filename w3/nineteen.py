s="abcd"

def check(s):
    if " " in s:
        l=s.split()
        return l
    elif "," in s:
        l=s.split(",")
        return l
    else:
        return s[1::2]

print(check(s))