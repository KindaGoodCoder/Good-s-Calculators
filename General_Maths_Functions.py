def numbercheck(number):
    try:
        float(number)
    except:
        return False
    return True

def intcheck(number):
    try:
        float(number)
    except:
        return False
    return float(number).is_integer()

def floatcheck(number):
    return True if numbercheck(number) and not intcheck(number) else False        

def intinator(number,roundby=2):
    if numbercheck(number):
        number = round(number,roundby)
        if float(number).is_integer():
            return int(number)
        return float(number)
    raise ValueError("Requires a 'float' or 'int' object")

def ezinput(msg):
    return input(msg).strip().lower()