#Calculator
from math import pi,sqrt
from General_Maths_Functions import *
#Cones

def verify(str):
    str = float(input(str+" "))
    if str < 0 and not "": raise ValueError
    return str

if __name__ == "__main__":    
    while True:
        try:
            match ezinput("Shape "):
                case "cone":

                    
                    radius = verify("Radius length")
                    length = verify("Length of edge")
                    height = verify("Length of height")

                    print("Volume is",(pi*height*radius**2)/3)
                    print("Surface Area is",pi*radius*(radius+length))

                case "cube":
                    side = verify("Side length")

                    if side:
                        print("Volume is ", side**3)
                        print("Surface area is", 6*side**2)
                    else:
                        volume = verify("Volume")
                        if not volume: 
                            sarea = verify("Surface area")
                            print("Side is",sqrt(sarea/6))
                        else: print("Side is",side**(1/3))
                        
                        
                case "square pyramid":                    
                    side = verify("side of base")
                    height = verify("pendicular height")
                    sheight = verify("Slant height")

                    print("Volume is",(side**2*height)/3)
                    if not sheight:
                        sheight = sqrt((side/2)**2+height**2)
                    print("Surface area is",side**2+4*(0.5*side*sheight))

                case "rectangular pyramid":                    
                    side = verify("Area of base")
                    height = verify("pendicular height")
                    sheight = verify("Slant height")

                    print("Volume is",(side*height)/3)
                    # if not sheight:
                    #     sheight = sqrt((side/2)**2+height**2)
                    # print("Surface area is",side**2+4*(0.5*side*sheight))

                case "trigular pyramid":
                    base = verify("Size of base")
                    height = verify("Pendipencular height")

                    print("Volume is", (base*height)/3)
                    # print("Surface area is", )

                case "sphere":
                    radius = verify("Radius Length ")

                    print("Volume is",4*pi*radius**2)
                    print("Surface Area is",4*(pi*radius**3)/3)
                case _:
                    pass

        except ValueError:
            print("Not a valid number \n")
            continue