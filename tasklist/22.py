l=[12,24,35,70,88,120,155]
li=[l[i] for i in range(len(l)) if i not in [0,4,5]]
print(li)