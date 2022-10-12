from multiprocessing.sharedctypes import Value
from General_Maths_Functions import *
from pyperclip import copy
from math import log

roundint = 2
simplemode = False
compoundmode = False
copymode = True

while True:
    match ezinput("Simple or compound "):
        case 'simple':
            while True:
                try:
                    P = intinator(input("\nP "))
                    R = intinator(input("R "))
                    N = intinator(input("N ")
                except ValueError:
                    print("Invalid input, please try again")
                    continue
                I = intinator(P*(R/100)*N)
                copy(f'${I}')
                print(f"Interest: ${I}")
                print(f"Total: ${I+P}",'\n')
        case 'compound':
            while True:
                try:
                    P = intinator(input("\nP "))
                    R = intinator(input("R "))
                    N = intinator(input("N "))
                except ValueError:
                    print("Invalid input, please try again")
                    continue
                I = intinator(P*(1+(R/100))**N,roundint)
                copy(f'${I}')
                print(f"I: ${I-P}\n")
                print(f"Total: ${I}\n")
        case 'reverse':
            method = ezinput("Solve for Simple or compound ")
            if method == 'simple':
                while True:
                    solve_variable = input("Solve for Principal, rate or time period ").lower().strip()
                    if solve_variable == "principal" or solve_variable == "p":
                        r = input("Rate ")
                        if r == 'exit':
                            print()
                            break
                        n = ezinput("Time period ")
                        if n == 'exit':
                            print()
                            break
                        FV = ezinput(input("Interest "))
                        if FV == 'exit':
                            print()
                            break
                        if (numbercheck(r) and numbercheck(n) and numbercheck(FV)):
                            r = float(r)
                            n = float(n)
                            FV = float(FV)
                            p = round(FV/(r/100*n),roundint)
                            if copymode:
                                copy(f'${p}')
                            print(f"The present value is ${p}\n")
                    elif solve_variable == "time" or solve_variable == "t" or solve_variable == "n":
                        r = input("Rate ")
                        if r == 'exit':
                            print()
                            break
                        FV = ezinput("Interest ")
                        if FV == 'exit':
                            print()
                            break
                        PV = ezinput("Principal ")
                        if PV == 'exit':
                            print()
                            break
                        if (numbercheck(r) and numbercheck(FV) and numbercheck(PV)):
                            r = float(r)
                            FV = float(FV)
                            PV = float(PV)
                            n = round(FV/(r/100*PV),roundint)
                            if copymode:
                                copy(n)
                            print(f"The time period is {n} units of time")
                    elif solve_variable == "rate" or solve_variable == "r":
                        n = input("Time period ")
                        if n == 'exit':
                            print()
                            break
                        FV = ezinput("Interest ")
                        if FV == 'exit':
                            print()
                            break
                        PV = ezinput("Principal ")
                        if PV == 'exit':
                            print()
                            break
                        if (numbercheck(n) and numbercheck(FV) and numbercheck(PV)):
                            n = float(n)
                            FV = float(FV)
                            PV = float(PV)
                            r = str(f'{round((FV/(n*PV))*100,roundint)}%')
                            if copymode:
                                copy(r)
                            print(f"The interest rate is {r}")
            elif method == 'compound':
                while True:
                    solve_variable = ezinput("Solve for Principal, rate or time period ")
                    if solve_variable == 'rate' or solve_variable == 'r':
                        FV = input("Future Value ")
                        if FV == 'exit':
                            print()
                            break
                        PV = input("Principal ")
                        if PV == 'exit':
                            print()
                            break
                        n = input("Time period ")
                        if n == 'exit':
                            print()
                            break
                        if (numbercheck(FV) and numbercheck(PV) and numbercheck(n)):
                            FV = float(FV)
                            PV = float(PV)
                            n = float(n)
                            r = round(100*(((FV/PV)**(1/n))-1),roundint)
                            if copymode:
                                copy(f'{intinator(r)}%')
                            print(f"The rate is {intinator(r)}%\n")
                    elif solve_variable == 'principal' or solve_variable == 'p':
                        FV = input("Future Value ")
                        if FV == 'exit':
                            print()
                            break
                        r = input("Rate ")
                        if r == 'exit':
                            print()
                            break
                        n = input("Time period ")
                        if n == 'exit':
                            print()
                            break
                        if (numbercheck(FV) and numbercheck(r) and numbercheck(n)):
                            FV = float(FV)
                            r = float(r)
                            n = float(n)
                            p = round(FV/(1+(r/100))**n,roundint)
                            if copymode:
                                copy(f'${p}')
                            print(f"The rate is ${p}\n")
                    elif solve_variable == 'time' or solve_variable == 'n' or solve_variable == 't':
                        FV = input("Future Value ")
                        if FV == 'exit':
                            print()
                            break
                        PV = input("Principal ")
                        if FV == 'exit':
                            print()
                            break
                        r = input("Rate ")
                        if r == 'exit':
                            print()
                            break
                        if (numbercheck(FV) and numbercheck(r) and numbercheck(PV)):
                            FV = float(FV)
                            r = float(r)
                            PV = float(PV)
                            n = round(log(FV/PV)/log(1+(r/100)),roundint)
                            if copymode:
                                copy(n)
                            print(f"The time period is {n} units of time\n")
                    elif solve_variable == 'exit':
                        print()
                        break
        case 'settings':
            x = "Accepted"
            while True:
                roundintinput = input("Round to which number ")
                if intcheck(roundintinput):
                    roundintinput = int(roundintinput)
                    if roundint > 0:
                        roundint = roundintinput
                        print(x,"\n")
                        break
                    else:
                        print("Only positive whole numbers are accepted\n")
                elif roundintinput == '':
                    break
                else:
                    roundintinput = ''
                    print("You did not enter a valid number, please enter a whole positive number\n")
            while True:
                copymodeinput = ezinput("Would you like the answers to be copied to your clipboard ")
                if copymodeinput == 'yes':
                    copymode = True
                    print(x)
                    break
                elif copymodeinput == 'no':
                    copymode = False
                    print(x)
                    break
                elif copymodeinput == '':
                    break
                else:
                    print("You did not enter a valid response, yes or no\n")
            while True:
                compoundmodeinput = ezinput(input("For compound interest, include first principal, yes or no?"))
                if compoundmodeinput == 'no':
                    compoundmode = True
                    print(x)
                    break
                elif compoundmodeinput == 'yes':
                    compoundmode = False
                    print(x)
                    break
                elif compoundmodeinput == '':
                    break
                else:
                    compoundmodeinput == ''
                    print("You did nor enter a valid response, please try again")
            while True:
                simplemodeinput = ezinput("For simple interest, include first principal, yes or no?")
                if simplemodeinput == 'yes':
                    simplemode = True
                    print(x)
                    break
                elif simplemodeinput == 'no':
                    simplemode = False
                    print(x)
                    break
                elif simplemodeinput == '':
                    break
                else:
                    simplemodeinput = ''
                    print("You did nor enter a valid response, please try again")
