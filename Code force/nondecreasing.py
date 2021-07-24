x=int(input())
str1=input()
str1=list(str1.split(" "))
count=[]
c=0
for i in range(x-1):
    if(str1[i]>=str1[i+1]):
        c+=1
    else:
        count.append(c)
        c=0
        i=i-1
print(count)
    
