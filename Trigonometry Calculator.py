from math import cos, sin, tan, acos, asin, atan,degrees,radians
from General_Maths_Functions import numbercheck
method = ''

while True:
    mode = input("Inverse or normal functions ").lower()
    if mode == 'normal':
        while True:
            method = input("Sine, Cosine or Tangent ").lower()
            exiting = f"Now exiting {mode} {method} mode\n"
            if method == 'sine':
                Solve_Side = input("Solve for Opposite or Hypotenuse ").lower()
                if Solve_Side == "hypotenuse":
                    angle = input("Size of angle ")
                    if angle == 'exit':
                        print(exiting)
                        break
                    side = input("Length of Opposite Side ")
                    if side == 'exit':
                        print(exiting)
                        break
                    if (numbercheck(angle) and numbercheck(side)) == True:
                        angle = float(angle)
                        side = float(side)
                        print("The hypotenuse side is",round(side/sin(radians(angle)),2),'\n')
                    else:
                        print("One of the sides are not a valid number\n")
                elif Solve_Side == "opposite":
                    angle = input("Size of angle ")
                    side = input("Length of Hypotenuse Side ")
                    if (numbercheck(angle) and numbercheck(side)) == True:
                        angle = float(angle)
                        if side == 'exit':
                            print(exiting)
                            break
                        side = float(side)
                        if side == 'exit':
                            print(exiting)
                            break
                        print("The opposite side is",round(side*sin(radians(angle)),2),'\n')
                    else:
                        print("One of the sides are not a valid number")
                elif Solve_Side == 'exit':
                    Solve_Side == ''
                    print(exiting)
                    break
                else:
                    print("You did not enter a valid mode, please select one of the modes\n")
            elif method == 'cosine':
                Solve_Side = input("Solve for Adjacent or Hypotenuse ").lower()
                if Solve_Side == 'adjacent':
                    angle = input("Size of angle ").lower()
                    if angle == 'exit':
                        print(exiting)
                        break
                    side = input("Length of Hypotenuse ").lower()
                    if side == 'exit':
                        print(exiting)
                        break
                    if (numbercheck(angle) and numbercheck(side)) == True:
                        angle = float(angle)
                        side = float(side)
                        print("The Adjacent side is",round(side*cos(radians(angle)),2),'\n')
                    else:
                        print("One of the inputs were not a valid number, please try again\n")
                elif Solve_Side == 'hypotenuse':
                    angle = input("Size of angle ").lower()
                    if angle == 'exit':
                        print(exiting)
                        break
                    side = input("Length of adjacent side ").lower()
                    if side == 'exit':
                        print(exiting)
                        break
                    if (numbercheck(angle) and numbercheck(side)) == True:
                        angle = float(angle)
                        side = float(side)
                        print("The Hypotenuse side is",round(side/cos(radians(angle)),2),'\n')
                    else:
                        print("One of the inputs were not a valid number, please try again\n")
                elif Solve_Side == 'exit':
                    print(exiting)
                    break
                else:
                    print("You did not enter a valid mode, please select one of the modes\n")
            elif method == 'tangent':
                Solve_Side = input("Solve for Opposite or Adjacent ").lower()
                if Solve_Side == 'opposite':
                    angle = input("Size of angle ").lower()
                    if angle == 'exit':
                        print(exiting)
                        break
                    side = input("Length of adjacent side ").lower()
                    if side == 'exit':
                        print(exiting)
                        break
                    if (numbercheck(side) and numbercheck(angle)) == True:
                        angle = radians(float(angle))
                        side = float(side)
                        print("The length of the Opposite Side is",round(side*tan(angle),2),'\n')
                    else:
                        print("One of the inputs were not a valid number, please try again\n")
                elif Solve_Side == 'adjacent':
                    angle = input("Size of angle ").lower()
                    if angle == 'exit':
                        print(exiting)
                        break
                    side = input("Length of opposite side ").lower()
                    if side == 'exit':
                        print(exiting)
                        break
                    if (numbercheck(side) and numbercheck(angle)) == True:
                        angle = radians(float(angle))
                        side = float(side)
                        print("The length of the adjacent Side is",round(side/tan(angle),2),'\n')
                    else:
                        print("One of the inputs were not a valid number, please try again\n")
                elif Solve_Side == 'exit':
                    print(exiting)
                    break
                else:
                    print("You did not enter a valid mode, please select one of the modes\n")
            elif method == 'exit':
                print(exiting)
                break
            else:
                print("You did not enter a valid mode, please try again\n")
    elif mode == 'inverse':
        while True:
            method = input("Sine, Cosine or Tangent ").lower()
            exiting = f"Now exiting {mode} {method} mode\n"
            if method == 'sine':
                side = input("Opposite Side Length ").lower()
                if side == 'exit':
                    print(exiting)
                    break
                side2 = input("Hypotenuse Side Length ").lower()
                if side2 == 'exit':
                    print(exiting)
                    break
                if (numbercheck(side) and numbercheck(side2)) == True and float(side) < float(side2):
                    side = float(side)
                    side2 = float(side2)
                    print("The angle is",round(degrees(asin(side/side2)),2),'\n')
                elif not float(side) < float(side2):
                    print("The opposite side should be shorter than the hypotenuse side, please try again\n")
                else:
                    print("One of the inputs were not a valid number, please try again\n")
            elif method == 'cosine':
                side = input("Adjacent Side Length ")
                if side == 'exit':
                    print(exiting)
                    break
                side2 = input("Hypotenuse Side Length ")
                if side2 == 'exit':
                    print(exiting)
                    break
                if (numbercheck(side) and numbercheck(side2)) == True and float(side) < float(side2):
                    side = float(side)
                    side2 = float(side2)
                    print("The angle is",round(degrees(acos(side/side2)),2),'\n')
                elif not float(side) < float(side2):
                    print("The adjacent side should be shorter than the hypotenuse side, please try again\n")
                else:
                    print("One of the inputs were not a valid number, please try again\n")
            elif method == 'tangent':
                side = input("Opposite Side Length ")
                if side == 'exit':
                    print(exiting)
                    break
                side2 = input("Adjacent Side Length ")
                if side2 == 'exit':
                    print(exiting)
                    break
                if (numbercheck(side) and numbercheck(side2)) == True:
                    side = float(side)
                    side2 = float(side2)
                    print("The angle is",round(degrees(atan(side/side2)),2),'\n')
            elif method == 'exit':
                exiting = f"Now exiting {mode} {method} mode\n"
                print(exiting)
                break
            else:
                print("You did not enter a valid mode, please try again\n")
    else:
        print("You did not enter a valid mode, please try again\n")
