str1=input()
str2=input()
count=0
try:
    for i in range(len(str1)):
        if(str1[i]==str2[len(str1)-i-1]):
           count+=1
        else:
            break;
    if(count==len(str1)):
        print("YES")
    else:
        print("NO")
except:
    print("NO")
