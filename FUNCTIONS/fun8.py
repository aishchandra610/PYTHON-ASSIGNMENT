def fun(*a):
    sum=0
    for i in a:
        sum+=i
    avg=sum/len(a)
    return avg
s=fun(1,2,3,4,5)
print(s)