from General_Maths_Functions import numbercheck

while True:
    p=input("Number of protons")
    n=input("Number of neutrons")
    if intcheck(p) and intcheck(n):
        print((float(p)+float(n))*1.66054e-27)
    else:
        print("One of the variables given is not a valid integer, please try again")
