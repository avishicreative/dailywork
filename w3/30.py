l1=[['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
l=[]

for i in l1:
    l.append(len(("".join(i)).replace(" ","")))
print(l)
