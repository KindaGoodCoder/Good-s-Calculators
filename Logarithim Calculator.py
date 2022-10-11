#logarithims
from General_Maths_Functions import numbercheck, intinator
from math import log

def inputnum(txt): #Checks if input is valid
    txt = input("Enter "+txt)
    if numbercheck(txt):
        return float(txt)
    raise ValueError

#Info on inputs
print("Constant Means number with definate value E.g: 4 or the decimal equalivent of 1/8\n The base number refers to the base number with the variable power. E.g: Enter 2 if you have 2^x ")

while True:
    try:
        constant = inputnum("constant ")
        var = inputnum("base of the variable power ")
        if var == 1:
            print("Variable power cannot equal 1")
            raise ValueError
        
    except ValueError:
        print("Invalid Input, please try again\n")
        continue
    print(intinator(log(constant,var)),"\n")