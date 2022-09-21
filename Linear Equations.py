#Please note 2 kinds of commenting is used in this program, one with #
"""The other using multiline strings without function"""

from General_Maths_Functions import *
"""
inputinator(Takes a number and turns it into a integer if possible)
intcheck(Returns True if given variable is a whole number)
numbercheck(Returns True if given variable is a number, whole or not
"""
from fractions import Fraction
from decimal import Decimal
from math import sqrt, gcd
#Coodinate reader, outputs coodinates into a list
def inputinator(inputting):
    data = input(inputting)
    #this if statement checks if we're recieving a gradient instead of a coodinate
    if "second" in inputting:
        try:
            float(data)
        except:
            pass
        else:
            return intinator(round(float(data),3))
    try:
        data = tuple(map(float,data.strip().split(',')))
        #Quickly round and turn avaliable numbers into integers
        data = tuple([intinator(round(x,3)) for x in data])
        if len(data) > 2:
            raise
        data[1]
    except:
        print("Invalid sequence, please enter a readable number sequence. For example: 1,2")
        return False
    else:
        return data

while True:
    c1 =  inputinator("\nEnter first coordinate. E.g. 3,5 ")
    if c1 == False:
        continue
    #declare coodinates
    x1 = c1[0]
    y1 = c1[1]
    c2 =  inputinator("Enter second coordinate or enter gradient (as a lone number) to solve line equation ")
    if c2 == False:
        continue
    #gradient or coodinate.
    if not numbercheck(c2):
        x2 = intinator(c2[0])
        y2 = intinator(c2[1])
        del c2, c1
        """No longer need the coodinate as a whole
        Now to find the midpoint
        (Adding f before a string allows it to be "formatted". Adding a variable between {} will display it in a formatted string """
        print(f"""\nMidpoint of the line between the points is
        (x2+x1)÷2,(y2+y1)÷2
        ({x2}+{x1})÷2,({y2}+{y1})÷2
        {x2+x1}÷2,{y2+y1}÷2
Therefore the answer is {intinator((x1+x2)/2)},{intinator((y1+y2)/2)}
""")
        x = x2-x1
        y = y2-y1
        length = x**2+y**2
        #length. If the square root of the length is irrational, display as surd
        if intcheck(sqrt(length)):
            length = int(sqrt(length))
        else:
            length = f"√{length}"
        print(f"""Length of line between the points is
        √((x2-x1)^2+(y2-y1)^2)
        √(({x2}-{x1})^2+({y2}-{y1})^2)
        √({x}^2+{y}^2)
        √({x**2}+{y**2})
The answer would then be""", length,'\n')
        del x2,y2
        """no longer needed

        gradient solving"""
        if y == 0:
            gradient = "Undefined"
            print("Since the difference between y2 and y1 is 0, therefore")
        elif x == 0:
            gradient = 0
            print("The difference between x2 and x1 is 0, therefore")
        else:
            print(f"""The Gradient of the line is
            {y}÷{x}. This simplified would mean""")
            b = intinator(round(y/x,3))
            if intcheck(b):
                gradient = int(b)
            else:
                gradient = Fraction(Decimal(str(y/x)))
        print("The gradient of the line between the points is",gradient,'\n')
    else:
        #This else segment is in case the user wants to use a gradient instead of a second coodinate, to directly find out the equations
        b = gradient = c2
        x = 1
        y = c1[1]
        del c1,c2
    #special gradient requirements
    if gradient == "Undefined":
        print("This line cannot be simplifed into a equation")
    elif gradient == 0:
        print("The gradient equation of the line is y =",gradient)
        print(f"The general equation of the line is {gradient} - y = 0")
    else:
        #The good stuff. Aka Gradient Equations
        x = intinator(x)
        print("The equation of the line can be evaluated by first finding the y-intercept")

        """Gotta find the y-intercept, so I reversed engineered the equation
        y-y1=m(x+x1)"""

        print(f"""  The y-intercept can be found by:
            y1-(y÷x*x1)
            {y1}-({y}÷{x})*{x1}
            {y1}-{b}*{x1}
            {y1}-{round(b*x1,3)}
            = {round(y1-(b*x1),3)}
        Knowing this, we simply add it to the equation of y = mx (m being the gradient) and,""")
        yintercept = intinator(round(y1-(b*x1),3))
        if gradient == 1:
            gradient = ""
        elif gradient == -1:
            gradient = "-"
        if intcheck(b):
            #x2 decides if the x variable shows in a fraction format or not
            x2 = 'x'
        else:
            x2 = ''
            numerator = Fraction(Decimal(str(b))).numerator
            denominator = Fraction(Decimal(str(b))).denominator
            if numerator == 1:
                numerator = ''
            if numerator == -1:
                numerator == '-'
            gradient = f"{numerator}x/{denominator}"
            #making it look the best possible, no one wants to see 1x/3. We want x/3
        if yintercept < 0:
            #looks better than + -1.
            symbol = '-'
            yintercept *= -1
        else:
            symbol = '+'
        print(f"The gradient equation of the line is y = {gradient}{x2} {symbol} {yintercept}\n")
        #ax + by + c = 0
        #gradient * x -y + c, no fractions
        print("""The gradient equation can be translated into a general equations using the formula
            ax-by+c=0 where A is the gradient, A and B are constants, and all numbers are whole integers.")
            First we have to subtract y from each side, so the equation would equal zero. And then multiply all numbers to a point they are
            all whole numbers, and simply""")
        gradient = b
        del b
        #For clarification, b was the actual gradient in a usable varible. Gradient varible was the version changed for viewing.
        y = 1
        #By default b in ax+by+c should be one.
        while True:
            #My solution to making all numbers whole.
            if not (intcheck(gradient) and intcheck(yintercept)):
                gradient,yintercept,y = (intinator(round(x*10,3)) for x in (gradient,yintercept,y))
            else:
                break
        #by dividing all varibles by their gcd... we should have the most simplified terms for them
        simple = gcd(y,gcd(gradient,yintercept))
        gradient,yintercept,y = (intinator(x/simple) for x in (gradient,yintercept,y))
        if gradient < 0:
            gradient *= -1
            symbol2 = '-'
            symbol = '+'
        else:
            symbol2 = '+'
            symbol = '-'
        if gradient == 1:
            gradient = ''
        #Honestly I believe the code to simplfy it for the user is longer than the actual calucations
        if y == 1:
            y = ''
        print(f"The general equation of the line is {gradient}x {symbol} {y}y {symbol2} {yintercept} = 0")
