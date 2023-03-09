#Quadratic Calculator
from General_Maths_Functions import intinator

if __name__ == "__main__":
    print("""This calculator requires you to seperate the coefficients of each variable in the quadratic calculator.
For example: ax^2 + bx + c
x^2 + 2x + 1
a = 1
b = 2
c = 1""")

    try:
        func = lambda x: intinator(input(f"What is the {x} coefficient?"))
        a = func("a")
        b = func("b")
        c = func("c")
    except:
        print("Error")
    
    #(-b+-
    