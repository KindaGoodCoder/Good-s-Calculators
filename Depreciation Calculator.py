from General_Maths_Functions import numbercheck

while True:
    mode = input("Solve value or for variable").lower().strip()
    if mode == 'value':
        while True:
            exiting = f"Now exiting {mode} mode"
            p = input("Principal? ").strip()
            if p == 'exit':
                print
            r = input("Rate? ").strip()
            n = input("Time? ").strip()
            if (numbercheck(p) and numbercheck(r) and numbercheck(n)):
                p = float(p)
                r = float(r)
                try:
                    int(n)
                except:
                    n = float(n)
                else:
                    n = int(n)
                print(f"The value in {n} (specified amount) will be ${round(p*(1-(r/100))**n,2)}")
        else:
            print("One of the inputs were not a valid number")
    elif mode == 'variable':
        mode = input("What variable to solve? ")
