from General_Maths_Functions import *

def breakinput(msg):
    msg = ezinput(msg+"?\n> ")
    if msg == "exit":
        print(f"Now exiting {mode} mode\n")
        raise ValueError
    elif not numbercheck(msg):
        print("Invalid input\n")
        raise
    return float(msg)

while True:
    mode = ezinput("Solve value or for variable ")
    if mode == 'value':
        while True:
            try:
                p = breakinput("Principal")
                r = breakinput("Rate")
                n = intinator(breakinput("Time"))
                print(f"The value in {n} terms will be ${intinator(round(p*(1-(r/100))**n,2))}\n")
            except ValueError:
                break
            except:
                continue
    elif mode == 'variable':
        mode = input("What variable to solve? ")
