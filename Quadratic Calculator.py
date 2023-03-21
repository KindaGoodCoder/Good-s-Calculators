#Quadratic Calculator
from General_Maths_Functions import intinator
import math

if __name__ == "__main__":
    print("""This calculator requires you to seperate the coefficients of each variable in the quadratic calculator.
For example: ax^2 + bx + c
x^2 + 2x + 1
a = 1
b = 2
c = 1""")
    while True:
        try:
            a,b,c = (intinator(input(f"\nWhat is the {x} coefficient?\n> ").strip()) for x in ["a","b","c"])
        except ValueError:
            print("Invalid input, try again")
            continue
    
        try:
            plus,minus = (intinator((b*-1 + x * math.sqrt(b**2-4*a*c))/2*a) for x in [1,-1])
        except ValueError:
            print("Equation cannot be factorised")
            continue

        connect = "or"
        symbol = ""
        
        if plus == minus * -1 or plus == minus:            
            connect = ""
            minus = ""
            if plus == minus * -1:
                symbol = "+-"
        
        print(f"\nx = {symbol}{plus} {connect} {minus}")