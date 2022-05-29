d={}
a=int(input("enter"))
for i in range(0,a):
    x=int(input("enter"))
    y=int(input("enter"))
    d[x]=y
b={1:2}
d.update(b)
print(d)