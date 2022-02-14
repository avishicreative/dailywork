num=int(input("Enter the number:"))

def dic(num):
    dict={}
    for n in range(1,num+1):
        dict[n]=n*n
    return dict

print(dic(num))