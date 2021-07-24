n=int(input())
str1=input()
c=str1[0]
count=0
for i in str1[1:]:
    if(i==c):
        count+=1
    else:
        c=i
        
print(count)
        
