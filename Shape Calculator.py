from General_Maths_Functions import numbercheck
from math import pi, sqrt

def calculator(v1,v2):
    if v2:
        if (numbercheck(v1) and numbercheck(v2)):
            v2 = float(v2)
        else:
            return False
    if not numbercheck(v1):
        return False
    v1 = float(v1)
    if v2:
        if v1>0 and v2>0:
            return v1,v2
        else:
            return False
    else:
        if v1>0:
            return [v1]
def printer(operation):
    if o:
        print(*operation)
    else:
        print(failmsg)

failmsg = "Invalid variable entered. Please enter a Positive Whole Number"

print("""Avaliable Shapes:
Sphere
Pentagonal Prism (Pentagon Prism)
Circle
Cylinder
Hexagontal Prism (Hexagon Prism)
Square Pyramid""")
while True:
    mode = input("What shape ").strip().lower()
    print()
    if mode == "sphere":
        radius = input("Radius of sphere ")
        o = calculator(radius,False)
        if not o:
            print(failmsg)
            continue
        printer(("The Volume of the Sphere is",round((4/3)*pi*o[0]**3,2)))
    elif mode == "pentagonal prism" or mode == "pentagon prism":
        side = input("Side length ")
        length = input("Shape length ")
        o = calculator(side,length)
        if not o:
            print(failmsg)
            continue
        printer(("The Volume of the Pentagonal Prism is ",round(0.25*sqrt(5*(5+2*sqrt(5)))*o[0]**2*o[1],2)))
    elif mode == "cylinder":
        radius=input("Radius ")
        length=input("Length ")
        o = calculator(radius,length)
        if not o:
            print(failmsg)
            continue
        printer(("The volume of the Cylinder is",round(pi*o[0]**2*o[1],2)))
    elif mode == "circle":
        r=input("Radius ")
        o = calculator(r,False)
        if not o:
            print(failmsg)
            continue
        printer(("The area of the Circle is",round(pi*(o[0]**2),2)))        
    elif mode == "hexagontal prism" or mode == "hexagon prism":
        side=input("Side Length ")
        length=input("Length ")
        o = calculator(side,length)
        if not o:
            print(failmsg)
            continue
        printer(("The volume of the Hexagontal Prism is",round(((3*sqrt(3))/2)*o[0]**2*o[1],2)))
    elif mode == 'hexagon':
        side = input("Side length ")
        o = calculator(side,False)
        if not o:
            print(failmsg)
            continue
        printer(("The area of the shape is",round(((3*sqrt(3))/2*o[0]),2)))
    elif mode == 'square pyramid':
        area = float(input("Area of base "))
        height = float(input("Height of pyramid"))
        # o = calculator(area,height)
        # if not o:
        #     print(failmsg)
        #     continue
        print("The volume of the pyramid is",round((area*height)/3,2))
    else:
        print("You did not enter a valid shape to calculate the area of, please try again")
    print()
