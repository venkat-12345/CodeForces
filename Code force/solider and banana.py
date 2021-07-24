str1=input()
str1=list(str1.split(" "))
a=int(str1[0])
x=int(str1[1])
n=int(str1[2])
sum1=0
for i in range(1,n+1):
    sum1+=a*i
if(sum1>x):
    print(sum1-x)
else:
    print(0)
