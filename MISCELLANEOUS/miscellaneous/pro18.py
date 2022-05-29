L=[1,2,3,4]
try:
    print(L[9])
except IndexError as e:
    print("Please Check the index ",e)
print("Bye")