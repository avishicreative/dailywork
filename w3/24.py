i=[0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]

def maxm():
    l=[]
    for j in range(len(i)):
       l.append(max(i[:j+1]))
    return l
print(maxm())