from General_Maths_Functions import *

class coord():
    def __init__(self,tuple):
        self.x = tuple[0]
        self.y = tuple[1]

def coinput(txt):
    txt = input(txt)
    txt = tuple(map(float,txt.split(',')))
    if len(txt) != 2:
        raise ValueError

if __name__ == "__main__":
    while True:
        try:
            c1 = coord(coinput("\nEnter first coordinate. E.g. 3,5 "))
            c2 = coord(coinput("Enter second coordinate "))
        except:
            print("Invalid Input")
            continue