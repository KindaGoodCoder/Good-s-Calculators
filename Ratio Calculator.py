from General_Maths_Functions import intcheck
from math import gcd

def checkinput(txt):
    txt = input(txt+" Number\n> ")
    if not intcheck(txt):
        raise
    return int(txt)

while True:
    try:
        one = checkinput("First")
        two = checkinput("Second")
        divide = gcd(one,two)
        print(int(one/divide),':',int(two/divide))
    except:
        print("One of the inputs contains a non-number character. All characters must be a number")