from General_Maths_Functions import *
from fractions import Fraction
class coord():
    def __init__(self,tuple):
        self.x = tuple[0]
        self.y = tuple[1]

def coinput(txt):
    txt = tuple(map(float,input(txt).split(',')))
    if len(txt) != 2:
        raise ValueError
    return txt

if __name__ == "__main__":
    while True:
        try:
            c1 = coord(coinput("\nEnter first coordinate. E.g. 3,5 "))
            c2 = coord(coinput("Enter second coordinate "))
        except:
            print("Invalid Input")
            continue
        mid = lambda a, b: intinator((a+b)/2)
        print(f"\nMidpoint of the line between the points is ({mid(c1.x,c2.x)},{mid(c1.y,c2.y)})")
        x = c2.x - c1.x
        y = c2.y - c1.y
        length = intinator(x**2+y**2)
        length = int(length**(1/2)) if intcheck(length**(1/2)) else f"√{length}"
        print(f"pain {length}")
        if y == 0:
            gradient = "Undefined"
        elif x == 0:
            gradient = 0
        else:
            if x < 0:
                x *= -1
                y *= -1
            gradient = Fraction(intinator(y),intinator(x))
        print("The gradient of the line between the points is",gradient)
        yintercept = intinator(c1.y-(gradient*c1.x))
        symbol = '+'
        if gradient == 1:
            gradient = ""
        elif gradient == -1:
            gradient = "-"

        if yintercept < 0:
            symbol = '-'
            yintercept *= -1
        elif yintercept == 0:
            yintercept = symbol = ''
        print(f"The gradient equation of the line is y = {gradient}x {symbol} {yintercept}")