from General_Maths_Functions import *

def breakinput(msg):
    return float(ezinput(msg+"?\n> "))

while True:
    try:
        p = breakinput("Principal")
        r = breakinput("Rate")
        n = breakinput("Time")
        rn = (1-(r/100))**n
        match [p,r,n]:
            case [0,r,n]:
                v = breakinput("Final Value")
                print(f"Principal is {intinator(v/rn)}")
            case [p,0,n]:
                print(f"Rate is {intinator(100*((v/p)**1/n+1))}")
            case [p,r,0]:
                pass
            case [p,r,n]:
                print(f"The value in {intinator(n)} terms will be ${intinator(p*rn)}")
    except:
        print("Invalid Input")
        continue    
    finally:
        print()