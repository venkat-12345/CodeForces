n=int(input())
a=[]
b=[]
sum1=[]
a.append(0)
b.append(0)
for _ in range(n):
    str1=input()
    str1=list(str1.split(" "))
    a.append(int(str1[0]))
    b.append(int(str1[1]))
sum1.append(0)
for i in range(1,n+1):
    sum1.append(b[i]-a[i]+sum1[i-1])
sum1.sort()
print(sum1[-1])
