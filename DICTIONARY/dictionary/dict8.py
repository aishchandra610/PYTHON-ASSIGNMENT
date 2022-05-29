a={'name':'aishwarya','class':'A'}
b={}
n=input("enter the value")
for i,j in a.items():
    if(n!=j):
        b[i]=j
print(b)