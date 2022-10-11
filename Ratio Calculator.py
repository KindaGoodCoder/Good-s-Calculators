from General_Maths_Functions import *
from math import gcd

def checkinput(txt):
    txt = input(txt+" Number\n> ").strip()    
    if not numbercheck(txt):
        raise
    if floatcheck(txt):
        while True:
            txt *= 10
            print(txt)
            if intcheck(txt):
                break
    return int(txt)

while True:
    # try:
        one = checkinput("First")
        two = checkinput("Second")
        divide = gcd(one,two)
        print(int(one/divide),':',int(two/divide))
    # except:
        print("One of the inputs contains a non-number character. All characters must be a number")