for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    x=0
    y=0
    for i in range(1,n):
        if(l[i]>l[i-1]):
            break
        else:
            y=i
    print(len(l)-y+x-1)
