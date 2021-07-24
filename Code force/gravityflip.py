k=int(input())
l=list(map(int,input().strip().split()))[:k]
l.sort()
for i in l:
       print(i,end=" ")
