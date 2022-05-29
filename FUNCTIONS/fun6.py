def switch(x, y):
    x, y = y, x

    print("inside switch : ", end = ' ')

    print("x", x, "y=", y)

x= 5

y=7

print("x=", x, "y=", y)

switch(x, y) 
print("x=", x, "y=", y)