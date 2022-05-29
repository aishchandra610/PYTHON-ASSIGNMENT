try:
    n=int(input("Enter the number"))
    print(n**2+"Hello")
except TypeError as e:
    print("Please Check the datatype in expression",e)
print("Bye")