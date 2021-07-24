n=int(input())
str1=input()
str1=list(str1.split(" "))
l=[]
l.sort()
l.reverse()
for i in str1:
    l.append(int(i))
max1=sum(l)/2
sum1=0
i=0
while(sum1<=max1):
    sum1+=l[i]
    i+=1
    
    
print(i)

