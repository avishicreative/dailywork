l=[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]

for i in range(len(l)):
    for j in range(len(l)):
        if l[i]+l[j]==0:
            if i<j:
                print([i,j])

