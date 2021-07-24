for _ in range(int(input())):
    n=int(input())
    if(n<10):
        print(n)
    else:
        l=len(str(n))
        
        if(n<int("1"*l)):
            r=9*(l-2)
            r+=n//(int("1"*(l-1)))
        else:
            r=9*(l-1)
            r+=n//(int("1"*l))
        if(len(set(str(n)))==1):
            r-=1
        print(r)
