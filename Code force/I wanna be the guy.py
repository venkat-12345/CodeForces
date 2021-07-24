n=int(input())
l=list(map(int,input().split()))
l+=list(map(int,input().split()))
l=list(set(l))
l.sort()
if(l[0]==0):
    l=l[1:]

#print(l,list(range(1,n+1)))
if(l==list(range(1,n+1))):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
