n=int(input())
count=0
l1=[]
l2=[]
l3=[]
sum1=0
for i in range(n):
    str1=input()
    str1=list(str1.split(" "))
    l1.append(int(str1[0]))
    l2.append(int(str1[1]))
    l3.append(int(str1[2]))
for i in range(n):
    sum1+=l1[i]
if(sum1!=0):
    print("NO")
else:
    for i in range(n):
        sum1+=l2[i]
    if(sum1!=0):
        print("NO")
    else:
        for i in range(n):
            sum1+=l3[i]
        if(sum1!=0):
            print("NO")
        else:
            print("YES")
        
    
    
        
