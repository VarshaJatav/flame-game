

l1=list(input("Enter first name:  "))
l2=list(input("Enter second name:  "))
i=0
while(i<len(l1)):
    for j in range(0,len(l2)):
        if l1[i]==l2[j]:
            l1.pop(i)
            l2.pop(j)
            i=i-1
            break
    i+=1
num=len(l1)+ len(l2)
l=['Friends','Love','Affection','Marriage','Enemy','Sibling']

c=0
while(len(l)!=1):
    for i in range(0,num):
        if c>=len(l):
            c=0
        c+=1
    c=c-1
    l.pop(c)
    
print("-----------------",l[0],"------------------")