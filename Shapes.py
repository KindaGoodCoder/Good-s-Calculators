#Calculator
from math import pi
#Cones
while True:
    match input("Mode ").lower():
        case "cone":
            radius = float(input("Radius length "))
            length = float(input("Length of edge "))
            height = float(input("Length of height "))
            print("Volume `is`",(pi*height*radius**2)/3)
            print("Surface Area is",pi*radius*(radius+length))
        case "square pyramid":
            side = float(input("side of base "))
            height = float(input("pendicular height "))
            pheight = float(input("Slant height "))
            print("Volume is",(side**2*height)/3)
            # print("Surface area is",side**2+2*side*)
        case "trigular pyramid":
            base = float(input("Size of base "))
            height = float(input("Pendipencular height "))
            print("Volume is", (base*height)/3)
        case "sphere":
            radius = float(input("Radius Length "))
            print("Volume is",4*pi*radius**2)
            print("Surface Area is",4*(pi*radius**3)/3)
        #case