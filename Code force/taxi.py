n=int(input())
str1=input()
str1=list(str1.split(" "))
str1.sort()
_1,_2,_3,_4=0,0,0,0
for i in str1:
    if(i=='1'):
        _1+=1
    elif(i=='2'):
        _2+=1
    elif(i=='3'):
        _3+=1
    else:
        _4+=1
if(_2%2==0):
    _2=_2//2
else:
    _2=(_2//2)+1
        
sum1=_4+_3+_2
k=_1-_3
if(_2%2!=0 and k>0):
    k=k-2
if(k<0):
    k=0
if(k>4):
    sum1+=k//4+k%4
else:
    sum1+=1
print(sum1)


    
    
