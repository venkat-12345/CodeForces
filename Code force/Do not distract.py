for _ in range(int(input())):
    n=int(input())
    s=input()
    l=[]
    t=s[0]
    i=0
    flag=0
    while(i<n):
        if(t==s[i]):
            i+=1
        else:
            l.append(t)
            t=s[i]
        if(t in l):
            flag=1
            break
    print("NO") if flag else print("YES")
