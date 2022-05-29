fileout = open("Student1.txt", "w")
for i in range(5):

    name = input ("Enter name of student :")

    fileout.write(name)

    fileout.write('\n') 

fileout.close()