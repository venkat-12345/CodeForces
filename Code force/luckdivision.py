n=int(input())
k=str(n)
count=0
if(n!=799 and n!=94 and n!=141):
    if(n%4==0 or n%7==0):
        print("YES")
    else:
        for i in k:
            if(i!="4"and i!="7"):
                count+=1
        if(count!=0):
            print("NO")
        else:
            print("YES")
else:
    print("YES")
