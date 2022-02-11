l= [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]

def check(l):
    sum=0
    for i in l:

        sum=sum+i
    if sum==0:
      return True
    else:
      return False

out=[]
for i in l:
    out.append(check(i))
print(out)