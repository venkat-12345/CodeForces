n=int(input())
x=0
for i in range(n):
    b=input()
    if(b=="X++" or  b=="++X"):
        x=x+1
    elif(b=="X--" or b=="--X"):
        x=x-1
print(x)
    
