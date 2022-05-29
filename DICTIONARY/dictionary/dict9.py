a={}
n=int(input("enter"))
for i in range(0,n):
    x=input("enter")
    y=input("enter")
    a[x]=y
val=input("enter the value")
for i,j in a.items():
    if(j==val):
        a.pop(i)
        break
print(a)