str1=input()
x=0
for i in str1:
    if(i=='4'):
        x+=1
    elif(i=='7'):
        x+=1
    else:
        pass
if(x==4 or x==7):
    print("YES")
else:
    print("NO")
