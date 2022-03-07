import math
while True:
    mode = input("Solve for hypotenuse or side ").lower()
    if mode == 'hypotenuse':
        a = float(input("A side "))
        b = float(input("B side "))
        print("c =", round(math.sqrt(a**2+b**2),2))
    elif mode == 'side':
        c = float(input("C side "))
        a = float(input("A side "))
        if c <= a:
            print("I think you made a mistake, C(The hypotenuse, or longer side)should be bigger than A")
        else:
            print("B =", round(math.sqrt(c**2-a**2),2))
