from General_Maths_Functions import *
from math import log

def breakinput(msg):
    return float(ezinput(msg+"?\n> "))
    
if __name__ == "__main__":
    while True:
        try:
            p = breakinput("Principal")
            r = breakinput("Rate")
            n = breakinput("Time")
            rn = (1-(r/100))**n
            match [p,r,n]:
                case [0,r,n]:
                    v = breakinput("Final Value")
                    print(f"Principal is ${intinator(v/rn)}")

                case [p,0,n]:
                    v = breakinput("Final Value")
                    print(f"Rate is {intinator(100*(1-(v/p)**(1/n)))}%")

                case [p,r,0]:
                    v = breakinput("Final Value")
                    print(f"Time is {intinator(log(v/p,r-1))}")

                case [p,r,n]:
                    print(f"The value in {intinator(n)} terms will be ${intinator(p*rn)}")
        except:
            print("Invalid Input")
            continue    
        finally:
            print()