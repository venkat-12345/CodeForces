str1=input()
str1=list(str1.split("+"))
str1.sort()
str2=""
for i in str1:
    str2+=i+"+"
print(str2[:-1])

    
