def retSeries (init, step):
     return init, init+step, init+2*step, init+3*step

ini= int(input("Enter initial value of the AP series :"))
st=int(input("Enter step value of the AP series :"))

print("Series with initial value", ini, "& step value", st, "goes as:") 
t1, t2, t3, t4= retSeries (ini, st)

print(t1, t2, t3, t4)