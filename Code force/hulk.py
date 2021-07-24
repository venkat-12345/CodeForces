k=int(input())
s1="I hate that "
s2="I love that "
s3=""
for i in range(k):
    if(i%2==0):
        s3+=s1
    else:
        s3+=s2
s3=s3[:-5]
s3+="it"
print(s3)




