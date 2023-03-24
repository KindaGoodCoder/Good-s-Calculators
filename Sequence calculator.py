#Sum of arthmetic sequence
from General_Maths_Functions import *

if __name__ == "__main__":
    while True:

        match ezinput("Arthmetic or geometric? "):

            case "artmethic":
                match ezinput("Find or Sum? "):

                    case "sum":
                        while True:
                            try:
                                inputting = lambda x: x*2
                                first,n,nterm = (ezinput(f"{term} term\n> ") for term in ["First","N","Value of Nth"])
                                if "exit" in [first,n,nterm]: break
                                first,n,nterm = map(intinator,[first,n,nterm])
                            except ValueError:
                                print("Invalid input")
                                continue

                            print(f"Sum of {n} terms is {(n/2)*(first+nterm)}")