from General_Maths_Functions import numcheck

def checkinput(txt)
    if not numcheck(txt)
        raise
    return float(txt)

while True:
    try:
        one = checkinput("First")
        two = checkinput("Second")
        divide = math.gcd(one,two)
        print(int(one/divide),':',int(two/divide))
    else:
        print("One of the inputs contains a non-number character. All characters must be a number")