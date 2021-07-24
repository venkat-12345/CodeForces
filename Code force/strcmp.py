str1=input()
str2=input()
str1=str1.casefold()
str2=str2.casefold()
sum1=0
for i in range(len(str1)):
    sum1=ord(str1[i])-ord(str2[i])
    if(sum1!=0):
        break
if(sum1>0):
    print("1")
elif(sum1<0):
    print("-1")
else:
    print("0")
