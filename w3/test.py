""""

sen= "Fear leads to anger; anger leads to hatred; hatred leads to conflict; conflict leads to suffering."
def extract(sent):
    sentence=sent.replace(';','')
    words=sentence.split()
    c1=0
    rwords=[]
    for w in words:
        if w in sentence:
            c1+=1
        if c1>1:
            rwords.append(w)
            reword=set(rwords)
    return reword
print("#".join(extract(sen)))
"""""

"""""
def extract2(lis):
    num=[0,1,2,3,4,5,6,7,8,9]
    out=[]
    for w in lis:
        if w.istitle() and w[0] not in ['A','E','I','O','U']:
            if w.isalpha():
                out.append(w)

    return out

print(extract2(['Avish','Dhruvil','raj','Ra6ii']))
"""""

"""""
def extractnum(lis):
    out=[]
    for n in lis:
        if (n%1000)%2==0 and (n/1000)%2!=0:
            if 999<n<10000 and (n%3==0 or n%7==0):
                out.append(n)
    return out

print(extractnum([1000,200000,1002,7000]))

"""
def iterdict2(d):
    for k, v in d.items():
        if type(v) == dict:
            iterdict2(v)
            if k=='tl'or k=='sen-dev'or k=='jun-dev':
                 for k1,v1 in v.items():
                   if v1['exp']>4:
                       print(k1)

def iterdict3(d):
    for k, v in d.items():
        if type(v) == dict:
            iterdict3(v)
            if k=='tl'or k=='sen-dev'or k=='jun-dev':
                 for k1,v1 in v.items():
                   if 3<v1['exp']<4.5:
                       v1['exp']=4.6
                       print(k1)


def iterdict4(d):
    for k, v in d.items():
        if type(v) == dict:
            iterdict4(v)
            if k=='tl':
                 for k1,v1 in v.items():
                   if v1['exp']<1:
                       print("N/A")
                   else:
                       print(k1,":",v1)

def iterdict6(d):
    for k, v in d.items():
        if type(v) == dict:
            iterdict6(v)
            if k=='tl'or k=='sen-dev'or k=='jun-dev':
                 for k1,v1 in v.items():
                   if v1['exp']<2:
                       print(k1)

def iterdict7(d):
    for k, v in d.items():
        if type(v) == dict:
            iterdict7(v)
            if k=='edge':
                print(k,v)



emp={
    "pro-man":{'rd':{
                        'tl':{'mark':{'exp':8},'amual':{'exp':8},'paul':{'exp':0},'tom':{'exp':8}},

                    },
              'ah':{
                        'tl':{"chris":{'exp':5},'pratt':{'exp':5},'emma':{'exp':5},'will':{'exp':5},'smith':{'exp':5}},

                    }
              },
    "manager":{

              'chris':{
                       'sen-dev':{'jenifer':{'exp':3.5},'scott':{'exp':3.5},'sophie':{'exp':3.5}},

                        },
              'will':{
                        'sen-dev':{'edge':{'exp':3},'rayan':{'exp':3.5}},

                    }
                },
    "reporting manager":{
              'smith':{
                        'sen-dev':{'walker':{'exp':2.7},'diana':{'exp':2.7}},

                        }
    },


    "mentor":{
             'mark':{
                     'jun-dev':{'leonardo':{'exp':1},'alexandera':{'exp':1}},

                     },
             'tom':{
                    'jun-dev':{'jerry':{'exp':1.5},'james':{'exp':1.6}},

                    },
            'paul':{
                    'sen-dev':{'fergal':{'exp':4.5}},

                    }
                }
}



#1
#for k in emp['pro-man'].keys():
#   print(emp['pro-man'][k]['tl'].keys())

#2

#print(iterdict2(emp))

"""""
for k in emp['pro-man'].keys():
    for k1 in emp['pro-man'][k]['tl'].keys():
        if emp['pro-man'][k]['tl'][k1]['exp']>4:
            print(emp['pro-man'][k]['tl'][k1])
"""
#3

#print(iterdict3(emp))

#for k in emp.keys():
#   for k1 in emp[k]:
#       for k2 in emp[k][k1]:
#           for k3 in emp[k][k1][k2]:
#               for k4 in emp[k][k1][k2][k3]:
#                   if (3<emp[k][k1][k2][k3][k4]<4.5):
#                       print(emp[k][k1][k2][k3][k4])

#4

#print(iterdict4(emp))
#for k in emp.keys():
#    for k1 in emp[k]:
#           for k2 in emp[k][k1]:
#               for k3 in emp[k][k1][k2]:
#                   for k4 in emp[k][k1][k2][k3]:
#                       if emp[k][k1][k2][k3][k4]<1:
#                           print(emp[k][k1][k2][k3],"N/A")
#                       else:
#                           print(emp[k][k1][k2][k3][k4])

#5
#emp['reporting manager']['rayan'] = emp['reporting manager']. pop('smith')
#print(emp)

#6

#print(iterdict6(emp))
"""""
for k in emp.keys():
   for k1 in emp[k]:
       for k2 in emp[k][k1]:
           for k3 in emp[k][k1][k2]:
               for k4 in emp[k][k1][k2][k3]:
                   if (emp[k][k1][k2][k3][k4]<2):
                        print(k3,emp[k][k1][k2][k3])

"""""
#7

print(iterdict7(emp))
"""""

for k in emp.keys():
    for k1 in emp[k]:
           for k2 in emp[k][k1]:
               for k3 in emp[k][k1][k2]:
                   if k3=='edge':
                       emp['pro-man']['rd']['tl'][k3]=(emp[k][k1][k2][k3])


print(emp)
"""""