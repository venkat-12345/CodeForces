str1=input()
x1=str1.find("H")
x2=str1.find("Q")
x3=str1.find("9")
if(str1[x1]=='H'or str1[x2]=='Q' or str1[x3]=='9'):
    print("YES")
else:
    print("NO")
