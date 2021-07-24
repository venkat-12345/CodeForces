for _ in range(int(input())):
    n=int(input())
    if(n==1):
        print(1)
    elif(n==2):
        print(-1)
    else:
        c=1
        l=[]
        flag=0
        while(c<=n*n):
            l.append(c+flag)
            if(flag==0):

                flag=1
            elif(flag==1):
                flag=-1
            else:
                flag=0
            c+=1
            
        for i in range(n*n):
            if((i+1)%n==0):
                print(l[i])
            else:
                print(l[i],end=" ")
            
