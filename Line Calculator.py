from General_Maths_Functions import *
from math import sqrt, gcd

def inputinator(inputting):
    data = input(inputting)
    if "second" in inputting:
        try:
            float(data)
        except:
            pass
        else:
            return float(data)
    try:
        data = tuple(map(float,data.strip().split(',')))
        data[1]
        if len(data) > 2:
            raise
    except:
        print("Invalid sequence, please enter a readable number sequence. For example: 1,2")
        return False
    return data

while True:
    c1 =  inputinator("\nEnter first coordinate. E.g. 3,5 ")
    if c1 == False:
        continue
    x1 = c1[0]
    c2 =  inputinator("Enter second coordinate or enter gradient (as a lone number) to solve line equation ")
    if c2 == False:
        continue
    if not numbercheck(c2):
        x2 = c2[0]
        y1 = c1[1]
        y2 = c2[1]
        del c2, c1
        print(f"\nMidpoint of the line between the points is ({intinator((x1+x2)/2)},{intinator((y1+y2)/2)})")
        length = intinator((x2-x1)**2+(y2-y1)**2)
        if intcheck(sqrt(length)):
            length = int(sqrt(length))
        else:
            length = f"√{length}"
        print("Length of line between the points is", length)
        x = x2-x1
        y = y2-y1
        del x2,y2
        if y == 0:
            gradient = "Undefined"
        elif x == 0:
            gradient = 0
        else:
            if x < 0:
                x *= -1
                y *= -1
            try:
                common = gcd(intinator(y),intinator(x))
            except:
                while not(intcheck(x) and intcheck(y)):
                    x *= 2
                    y *= 2
            common = gcd(intinator(y),intinator(x))
            y /= common
            x /= common
            if intcheck(y/x):
                gradient = intinator(round(y/x,3))
            else:
                gradient = f"{intinator(y)}/{intinator(x)}"
        print("The gradient of the line between the points is",gradient)
    else:
        y = c2
        x = 1
        gradient = ''
        y1 = c1[1]
        x1 = c1[0]
    if gradient == "Undefined":
        print("This line cannot be simplifed into a equation")
    elif gradient == 0:
        y = intinator(y)
        print("The gradient equation of the line is y =",y)
        print(f"The general equation of the line is y -",y,'= 0')
    else:
        gradient = round(y/x,3)
        c2 = round(y1-(gradient*x1),3)
        if gradient == 1:
            gradient = ""
        elif gradient == -1:
            gradient = "-"
        else:
            gradient = intinator(gradient)
        symbol = symbol2 = yintercept = ''
        if c2 < 0:
            symbol = '-'
            yintercept = intinator(c2 * -1)
        elif c2 != 0:
            yintercept = intinator(c2)
            symbol = '+'
        print(f"The gradient equation of the line is y = {gradient}x {symbol} {yintercept}")
        #ax + by + c = 0
        #gradient *x -y + c, no fractions
        gradient = intinator(y/x)
        y = 1
        if not (intcheck(gradient) and intcheck(yintercept)):
            while not (intcheck(gradient) or intcheck(yintercept)):
                y *= 2
                gradient *=2
                yintercept *=2
        if gradient < 0:
            gradient *= -1
            yintercept *= -1
            symbol = '+'
        else:
            symbol = '-'
        if gradient == 1:
            gradient = ''
        if yintercept:
            yintercept = intinator(float(yintercept))
            if yintercept < 0:
                yintercept *= -1
                symbol2 = '-'
            else:
                symbol2 = '+'
        if y == 1:
            y = ''
        print(f"The general equation of the line is {gradient}x {symbol} {y}y {symbol2} {yintercept} = 0")
