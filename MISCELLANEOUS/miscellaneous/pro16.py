try:
    fp=open("a.txt","r")
    try:
        fp.write("This is my test file")
    finally:
        print("Closing the file")
        fp.close()
except IOError as e:
    print("Error:",e)