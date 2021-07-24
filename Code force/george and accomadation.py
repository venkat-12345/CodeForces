k=int(input())
count=0
for i in range(k):
    str1=input()
    str1=list(str1.split(" "))
    if(int(str1[1])-int(str1[0])>=2):
        count+=1
    
print(count)
