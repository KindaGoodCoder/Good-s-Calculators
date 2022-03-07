def numbercheck(number):
    try:
        float(number)
    except:
        return False
    else:
        return True

def intcheck(number):
    try:
        float(number)
    except:
        return False
    else:
        return float(number).is_integer()

def intinator(number):
    if type(number) == 'float' or 'int':
        if number.is_integer():
            return int(number)
        else:
            return number
    else:
        raise ValueError("Requires a 'float' or 'int' object")

def ezinput(msg):
    return input(msg).strip().lower()