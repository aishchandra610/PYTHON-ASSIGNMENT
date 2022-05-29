def oct2others(n) :
    print("Passed octal number :",n)

    numString = str(n)

    decNum = int(numString, 8) 
    print("Number in Decimal :", decNum)

    print("Number in Binary:", bin(decNum))
    print("Number in Hexadecimal :", hex(decNum))

num= int(input("Enter an octal number :"))
oct2others(num)