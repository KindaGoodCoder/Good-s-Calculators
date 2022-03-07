import math

 #Put variables here
while True:
    one = input("first number ")
    two = input("second number ")
    three = input("third number... use 0 if none ")
#Run Code here
    if one.isnumeric() and two.isnumeric() and three.isnumeric():
        one = int(one)
        two = int(two)
        three = int(three)
        if three != 0:
            divide = math.gcd(one,two,three)
            print(int(one/divide),':',int(two/divide),":",int(three/divide))
        else:
            divide = math.gcd(one,two)
            print(int(one/divide),':',int(two/divide))
    else:
        print("One of the inputs contains a non-number character. All characters must be a number")
#Function here... only needed if a calculation is done several times
def calculation():
    print("MATHS!")

calculation()
