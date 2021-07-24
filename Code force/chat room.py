str1=input()
str0=""
str1=list(str1)
str1.sort()
for i in str1:
    str0+=i
c=str0[0]
str2=""+c
for i in str0[1:]:
    if(i=='h' or i=='e' or i=='l' or i=='o'):    
        if(c!=i):
            str2+=i
            c=i
x=str2.find("e")
if(str2[x:x+4]=="ehlo"):
    print("YES")
else:
    print("NO")

    
    
