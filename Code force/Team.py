n=int(input())
st=[]
count=0
fc=0
for i in range(n):
    b=input()
    st.append(b)
    st[i]=list(st[i].split(" "))
for i in range(n):
    for j in st[i]:
        count+=int(j)
    if(count>=2):
        fc=fc+1
        
print(fc)
