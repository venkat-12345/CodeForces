l=[]
n=int(input())
for i in range(n):
    b=input()
    l.append(b)
for i in range(n):
    k=len(l[i])
    if(k>10):
        print("%c%d%c"%(l[i][0],k-2,l[i][k-1]))
    else:
        print(l[i])

