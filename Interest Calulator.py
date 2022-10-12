from General_Maths_Functions import *
# from pyperclip import copy
from math import log

def copy(_):
    pass

copying = lambda a: copy(a) if copymode else 0 #little mini function

def intinput(txt):
    txt = ezinput(txt) 
    if txt == "exit":
        print("Exiting...\n")
        raise TypeError 
    return intinator(txt) #Either errors and raises ValueError or returns... choose one

def simple_reverseop(v1,v2):
    I = intinput("Interest ")
    I = I/(v1*v2)
    copying(I)
    return intinator(I,roundint)

def inputs():
    P = intinput("\nPrincipal ")
    R = intinput("Rate ")/100
    N = intinput("Time ")
    return [P,R,N]

if __name__ == "__main__":
    roundint = 2 #Default settings
    copymode = True 

    while True:
        match ezinput("Simple or compound "):
            case 'simple': #Simple interest calculator
                while True:
                    try:                        
                        match inputs():
                            case [0,R,N]: #If nothing put for P
                                print(f"> Principal: ${simple_reverseop(R,N)}")
                            case [P,0,N]: #If nothing put for R
                                print(f"> Rate: {intinator(simple_reverseop(P,N)*100)}%")
                            case [P,R,0]: #If nothing put for N
                                print(f"> Time: {simple_reverseop(R,P)}")
                            case [P,R,N]: #If all numbers have a value
                                I = intinator(P*R*N,roundint)
                                copying(I)
                                print(f"> Interest: ${I}")
                                print(f"> Total: ${I+P}",'\n')
                    except TypeError:
                        break
                    except ValueError:
                        print("Invalid input, please try again")
                        continue

            case 'compound': #Compound Interest Calculator
                while True:
                    try:
                        match inputs(): #Filter calculation

                            case [0,R,N]:
                                I = intinput("Total ")
                                P = I/(1+R)**N
                                copying(P)
                                print(f"> Principal: ${P}") #Calculate for Principal

                            case [P,0,N]:
                                I = intinput("Total Value ")
                                R = intinator(100*((I/P)**(1/N)-1),roundint) #Calculate for Rate
                                copying(R)
                                print(f"> Rate: {R}%")

                            case [P,R,0]:
                                if P < 0 or R < 0:
                                    print("No negative numbers") #You try performing logarithmics on a negative number
                                    continue
                                I = intinput("Total Value ")
                                N = intinator(log(I/P,R+1),roundint) #Calculate for Time. Use log() to find x if (R+1)^x = I/P
                                copying(N)
                                print(f"> Time: {N}")

                            case [P,R,N]:
                                I = intinator(P*(1+R)**N,roundint)
                                copying(I-P)
                                print(f"> Interest: ${I-P}")
                                print(f"> Total: ${I}\n")

                    except ValueError:
                        print("Invalid input, please try again")
                        continue
                    except TypeError:
                        break

            case 'settings': #Settings to change rounding number and whether to copy answer to clipboard
                R = ''
                while True:

                    roundint = 2
                    match ezinput("Round to how many decimal places "):
                        case "continue"|'':
                            break
                        case "exit":
                            print("Exiting...\n")
                            R = 'exit'
                            break
                        case roundint: #Reassign roundint to this number
                            if not intcheck(roundint):
                                roundint = 2
                                print("Invalid\n")
                                continue
                            roundint = int(roundint)
                            break

                if not R == "exit": #If roundint didn't call exit move on
                    while True:
                        match ezinput("Copy answers to clipboard "):
                            case "exit"|"continue"|'':
                                print("Exiting...\n")
                                break
                            case "y"|"yes"|"true":
                                copymode = True
                                break
                            case "n"|"no"|"false":
                                copymode = False
                                break
                            case _:              
                                print("Invalid input\n")