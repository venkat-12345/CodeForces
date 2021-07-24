str1=input()
str2=input()

str1=list(str1.split(" "))
n=int(str1[0])
k=int(str1[1])


str2=list(str2.split(" "))
l=[]
count=0
for i in str2:
    l.append(int(i))
if(l[0]>k):
    for i in range(len(l)):
        if(l[i]>k):
            count+=1
        else:
            break
elif(l[0]==k):
    for i in range(len(l)):
        if(l[i]==k):
            count+=1
        else:
            break
elif(l[0]<k and l[0]!=0):
    k=l[0]
    for i in range(len(l)):
        if(l[i]==k):
            count+=1
        else:
            break

  
print(count)
