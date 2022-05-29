import ast


def fact(f):
    if f==1:
        return 1
    else:
        return(f*fact(f-1))
a=fact(5)
print(a)