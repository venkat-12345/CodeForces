str1=input()
count1,count2=0,0
for i in str1:
    if i=="1":
        count1+=1
        count2=0
        if count1>=7:
            break
    else:
        count2+=1
        count1=0
        if count2>=7:
            break
if count1>=7 or count2>=7:
    print("YES")
else:
    print("NO")
    
