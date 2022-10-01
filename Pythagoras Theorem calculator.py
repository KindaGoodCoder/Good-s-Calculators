from math import sqrt
from General_Maths_Functions import *

def breakinput(msg):
    msg = input(msg+" side\n> ").strip()
    return float(msg)

while True:
    mode = ezinput("Solve for hypotenuse or side ")
    if mode == 'hypotenuse' or mode == "h":
        try:
            a = breakinput("A")
            b = breakinput("B")
            print(f"C = {intinator(sqrt(a*a+b*b))}")
        except:
            print("Invalid Input")
        print()
    elif mode == 'side':
        try:
            c = breakinput("C")
            a = breakinput("A")
            if c <= a:
                print("C should be longer than A")
            else:
                print(f"B = {intinator(sqrt(c*c-a*a))}")
        except:
            print("Invalid Input")
        print()
    else:
        print("Invalid input\n")