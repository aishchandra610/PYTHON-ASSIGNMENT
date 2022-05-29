fh = open("Result.det", "r")

count = 0 
rec = ""

while True :

    rec = fh.readline()

    if rec =="":

        break

    count = count + 1

print(count, rec, end = '') 
fh.close()